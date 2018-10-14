using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MathsCypher.Properties;

namespace MathsCypher
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private Dictionary<char, int> _mappings = new Dictionary<char, int>();
        private Random _random = new Random();

        private void frmMain_Load(object sender, EventArgs e)
        {
            ActiveControl = txtCodedMessageInput;

            loadSettings();
            populateMappingsList();
        }

        private void frmMain_FormClosed(object sender, FormClosedEventArgs e)
        {
            saveSettings();
        }

        private void saveSettings()
        {
            Settings.Default.CodedMessageInput = txtCodedMessageInput.Text;
            Settings.Default.MappingsList = string.Join(";",
                _mappings.Select(mapping => mapping.Key + "=" + mapping.Value).ToArray()
                );
            Settings.Default.Save();
        }

        private void loadSettings()
        {
            var mappings = Settings.Default.MappingsList;
            if (mappings == "")
                generateDefaultMappings();
            else
                extractMappings(mappings);

            txtCodedMessageInput.Text = Settings.Default.CodedMessageInput;
        }

        private void extractMappings(string mappings)
        {
            foreach (var mapping in mappings.Split(';'))
            {
                var splitMapping = mapping.Split('=');
                var key = Convert.ToChar(splitMapping[0]);
                var value = Convert.ToInt32(splitMapping[1]);
                _mappings.Add(key, value);
            }
        }

        private void populateMappingsList()
        {
            lvwMappings.Items.Clear();
            foreach (var mapping in _mappings)
            {
                lvwMappings.Items.Add(
                    new ListViewItem(
                        new[] { mapping.Value.ToString(), mapping.Key.ToString() }
                        )
                    );
            }
        }

        private void generateDefaultMappings()
        {
            _mappings.Clear();
            var number = 2;
            for (char letter = 'A'; letter <= 'Z'; letter++)
            {
                while (number.GetFactors().Count < 4)
                    number++;
                
                _mappings.Add(letter, number++);
            }
        }

        private void txtCodedMessageInput_TextChanged(object sender, EventArgs e)
        {
            regenerate();
        }

        private void cmdRegenerate_Click(object sender, EventArgs e)
        {
            regenerate();
        }

        private void regenerate()
        {
            rtfPuzzleOutput.Clear();
            createHeading();
            appendEncodedMessage();
            appendMappingsTable();
        }

        private void appendMappingsTable()
        {
            rtfPuzzleOutput.AppendText(string.Format("{0}{0}Here's a clue!{0}", Environment.NewLine));
            var index = 1;
            foreach (var mapping in _mappings)
            {
                var key = mapping.Key;
                var value = mapping.Value;
                var delimiter = index % 6 == 0 ? Environment.NewLine : "\t";
                rtfPuzzleOutput.AppendText(string.Format("{0} = {1}{2}{2}", value, key, delimiter));
                index++;
            }
        }

        private void appendEncodedMessage()
        {
            var colours = new[] { Color.Red, Color.Blue, Color.Green };
            var colourIndex = 0;
            foreach (char character in txtCodedMessageInput.Text.ToUpper())
            {
                var encoding = encodeCharacter(character);
                rtfPuzzleOutput.AppendText(encoding, colours[colourIndex]);

                colourIndex++;
                if (colourIndex >= colours.Length)
                    colourIndex = 0;
            }
        }

        private void createHeading()
        {
            rtfPuzzleOutput.SelectionAlignment = HorizontalAlignment.Center;
            rtfPuzzleOutput.AppendText("Maths Cypher" + Environment.NewLine, new Font("Arial", 24f, FontStyle.Bold));
            rtfPuzzleOutput.SelectionAlignment = HorizontalAlignment.Left;

            rtfPuzzleOutput.AppendText("Can you solve this puzzle?" + Environment.NewLine);
        }

        private string encodeCharacter(char character)
        {
            if (character == ' ' || character.Equals('\n'))
                return Environment.NewLine;

            if (!_mappings.ContainsKey(character))
                return character + "  ";

            var answer = _mappings[character];

            if (getRandomOperation() == Operation.MULTIPLICATION)
            {
                var multiplication = new Multiplication(answer, _random);
                return multiplication.ToString();
            }

            var division = new Division(answer, _random);
            return division.ToString();
        }

        private enum Operation {
            MULTIPLICATION,
            DIVISION
        }

        private Operation getRandomOperation()
        {
            var values = Enum.GetValues(typeof(Operation));
            return (Operation)values.GetValue(_random.Next(values.Length));
        }

        private void lvwMappings_AfterLabelEdit(object sender, LabelEditEventArgs e)
        {
            if (e.Label == null)
                return;

            int newNumber;
            if (!int.TryParse(e.Label, out newNumber))
            {
                cancelMappingEdit(e, "Expected an integer");
                return;
            }

            ListViewItem listItem = lvwMappings.Items[e.Item];
            if (e.Label == listItem.Text)
                return;

            if (_mappings.Values.Contains(newNumber))
            {
                cancelMappingEdit(e, "Duplicate number");
                return;
            }

            char letter = Convert.ToChar(listItem.SubItems[1].Text);
            _mappings[letter] = newNumber;
            regenerate();
        }

        private static void cancelMappingEdit(LabelEditEventArgs e, string failureMessage)
        {
            MessageBox.Show(failureMessage);
            e.CancelEdit = true;
        }

        private void cmdDefaultMappings_Click(object sender, EventArgs e)
        {
            generateDefaultMappings();
            populateMappingsList();
            regenerate();
        }

        private void cmdJumble_Click(object sender, EventArgs e)
        {
            var valueList = _mappings.Values.ToList().Shuffle();

            _mappings.Clear();
            var index = 0;
            for (char letter = 'A'; letter <= 'Z'; letter++)
            {
                _mappings.Add(letter, valueList[index++]);
            }

            populateMappingsList();
            regenerate();
        }

        private void cmdCopy_Click(object sender, EventArgs e)
        {
            rtfPuzzleOutput.SelectAll();
            rtfPuzzleOutput.Copy();
        }
    }
}
