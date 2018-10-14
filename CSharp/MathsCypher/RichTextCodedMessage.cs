using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace MathsCypher
{
    internal class RichTextCodedMessage
    {
        public RichTextCodedMessage(CodedMessage codedMessage, Random random, Dictionary<char, int> mappings)
        {
            _codedMessage = codedMessage;
            _mappings = mappings;
            _random = random;
        }

        private CodedMessage _codedMessage;
        private Dictionary<char, int> _mappings;
        private Random _random;

        public void Generate(RichTextBox richTextBox)
        {
            createHeading(richTextBox);
            appendEncodedMessage(richTextBox);
            appendMappingsTable(richTextBox);
        }

        private void appendMappingsTable(RichTextBox richTextBox)
        {
            richTextBox.AppendText(string.Format("{0}{0}Here's a clue!{0}", Environment.NewLine));
            var index = 1;
            foreach (var mapping in _mappings)
            {
                var key = mapping.Key;
                var value = mapping.Value;
                var delimiter = index % 7 == 0 ? Environment.NewLine : "\t";
                richTextBox.AppendText(string.Format("{0} = {1}{2}{2}", value, key, delimiter));
                index++;
            }
        }

        private void appendEncodedMessage(RichTextBox richTextBox)
        {
            var colours = new[] { Color.Red, Color.Blue, Color.Green };
            var colourIndex = 0;
            foreach (var encoding in _codedMessage.Generate())
            {
                richTextBox.AppendText(encoding, colours[colourIndex]);

                colourIndex++;
                if (colourIndex >= colours.Length)
                    colourIndex = 0;
            }
        }

        private void createHeading(RichTextBox richTextBox)
        {
            richTextBox.SelectionAlignment = HorizontalAlignment.Center;
            richTextBox.AppendText("Maths Cypher" + Environment.NewLine, new Font("Arial", 24f, FontStyle.Bold));
            richTextBox.SelectionAlignment = HorizontalAlignment.Left;

            richTextBox.AppendText("Can you solve this puzzle?" + Environment.NewLine);
        }
    }
}