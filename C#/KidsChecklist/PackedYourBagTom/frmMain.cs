using KidsCheckList.Properties;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KidsCheckList
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
            Icon = Properties.Resources.APP_ICON;
            picNoodle.Image = Properties.Resources.Noodle;
            lblNoodleSpeech.MaximumSize = new Size(picNoodle.Width / 3, 0);
            lblNoodleSpeech.BackColor = Color.Transparent;
            lblNoodleSpeech.Parent = picNoodle;
            lblNoodleSpeech.Location = picNoodle.PointToClient(PointToScreen(lblNoodleSpeech.Location));

            populateCheckList();
        }

        private void populateCheckList()
        {
            foreach (var item in Settings.Default.CheckList.Split(new[] { ';' }, StringSplitOptions.RemoveEmptyEntries))
                lvwCheckList.Items.Add(item);
        }

        private void setNoodleSpeech(string text)
        {
            lblNoodleSpeech.Text = text;
        }

        private void lvwCheckList_ItemChecked(object sender, ItemCheckedEventArgs e)
        {
            if (lvwCheckList.CheckedItems.Count == 0)
                setNoodleSpeech(Properties.Settings.Default.HaveYouText);
            else if (lvwCheckList.CheckedItems.Count == lvwCheckList.Items.Count)
            {
                setNoodleSpeech("Are you sure?!");
                cmdYesImSure.Visible = true;
            }
            else
                setNoodleSpeech("Good...");
        }

        private void cmdYesImSure_Click(object sender, EventArgs e)
        {
            cmdYesImSure.Visible = false;
            setNoodleSpeech("Okay you can play now.");
            tmrCloseForm.Enabled = true;
        }

        private void tmrCloseForm_Tick(object sender, EventArgs e)
        {
            Close();
        }

        private const int CP_NOCLOSE_BUTTON = 0x200;
        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams myCp = base.CreateParams;
                myCp.ClassStyle = myCp.ClassStyle | CP_NOCLOSE_BUTTON;
                return myCp;
            }
        }
    }
}
