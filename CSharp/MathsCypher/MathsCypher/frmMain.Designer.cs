namespace MathsCypher
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.HorizontalSplitContainer = new System.Windows.Forms.SplitContainer();
            this.TabControl = new System.Windows.Forms.TabControl();
            this.tabCodedMessage = new System.Windows.Forms.TabPage();
            this.txtCodedMessageInput = new System.Windows.Forms.TextBox();
            this.tabMappings = new System.Windows.Forms.TabPage();
            this.cmdJumble = new System.Windows.Forms.Button();
            this.cmdDefaultMappings = new System.Windows.Forms.Button();
            this.lvwMappings = new System.Windows.Forms.ListView();
            this.colNumber = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colLetter = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tabDifficulty = new System.Windows.Forms.TabPage();
            this.lblMaxDividendValue = new System.Windows.Forms.Label();
            this.txtMaxDividendValue = new System.Windows.Forms.TextBox();
            this.lblMaxFactorValue = new System.Windows.Forms.Label();
            this.txtMaxFactorValue = new System.Windows.Forms.TextBox();
            this.cmdCopy = new System.Windows.Forms.Button();
            this.cmdRegenerate = new System.Windows.Forms.Button();
            this.lblPuzzleOutput = new System.Windows.Forms.Label();
            this.rtfPuzzleOutput = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.HorizontalSplitContainer)).BeginInit();
            this.HorizontalSplitContainer.Panel1.SuspendLayout();
            this.HorizontalSplitContainer.Panel2.SuspendLayout();
            this.HorizontalSplitContainer.SuspendLayout();
            this.TabControl.SuspendLayout();
            this.tabCodedMessage.SuspendLayout();
            this.tabMappings.SuspendLayout();
            this.tabDifficulty.SuspendLayout();
            this.SuspendLayout();
            // 
            // HorizontalSplitContainer
            // 
            this.HorizontalSplitContainer.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.HorizontalSplitContainer.Location = new System.Drawing.Point(12, 12);
            this.HorizontalSplitContainer.Name = "HorizontalSplitContainer";
            this.HorizontalSplitContainer.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // HorizontalSplitContainer.Panel1
            // 
            this.HorizontalSplitContainer.Panel1.Controls.Add(this.TabControl);
            // 
            // HorizontalSplitContainer.Panel2
            // 
            this.HorizontalSplitContainer.Panel2.Controls.Add(this.cmdCopy);
            this.HorizontalSplitContainer.Panel2.Controls.Add(this.cmdRegenerate);
            this.HorizontalSplitContainer.Panel2.Controls.Add(this.lblPuzzleOutput);
            this.HorizontalSplitContainer.Panel2.Controls.Add(this.rtfPuzzleOutput);
            this.HorizontalSplitContainer.Size = new System.Drawing.Size(1115, 696);
            this.HorizontalSplitContainer.SplitterDistance = 209;
            this.HorizontalSplitContainer.TabIndex = 3;
            // 
            // TabControl
            // 
            this.TabControl.Controls.Add(this.tabCodedMessage);
            this.TabControl.Controls.Add(this.tabMappings);
            this.TabControl.Controls.Add(this.tabDifficulty);
            this.TabControl.Dock = System.Windows.Forms.DockStyle.Fill;
            this.TabControl.Location = new System.Drawing.Point(0, 0);
            this.TabControl.Name = "TabControl";
            this.TabControl.SelectedIndex = 0;
            this.TabControl.Size = new System.Drawing.Size(1115, 209);
            this.TabControl.TabIndex = 3;
            // 
            // tabCodedMessage
            // 
            this.tabCodedMessage.Controls.Add(this.txtCodedMessageInput);
            this.tabCodedMessage.Location = new System.Drawing.Point(4, 29);
            this.tabCodedMessage.Name = "tabCodedMessage";
            this.tabCodedMessage.Padding = new System.Windows.Forms.Padding(3);
            this.tabCodedMessage.Size = new System.Drawing.Size(1107, 176);
            this.tabCodedMessage.TabIndex = 0;
            this.tabCodedMessage.Text = "Message Input";
            this.tabCodedMessage.UseVisualStyleBackColor = true;
            // 
            // txtCodedMessageInput
            // 
            this.txtCodedMessageInput.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtCodedMessageInput.Location = new System.Drawing.Point(3, 3);
            this.txtCodedMessageInput.Multiline = true;
            this.txtCodedMessageInput.Name = "txtCodedMessageInput";
            this.txtCodedMessageInput.Size = new System.Drawing.Size(1101, 170);
            this.txtCodedMessageInput.TabIndex = 0;
            this.txtCodedMessageInput.TextChanged += new System.EventHandler(this.txtCodedMessageInput_TextChanged);
            // 
            // tabMappings
            // 
            this.tabMappings.Controls.Add(this.cmdJumble);
            this.tabMappings.Controls.Add(this.cmdDefaultMappings);
            this.tabMappings.Controls.Add(this.lvwMappings);
            this.tabMappings.Location = new System.Drawing.Point(4, 29);
            this.tabMappings.Name = "tabMappings";
            this.tabMappings.Padding = new System.Windows.Forms.Padding(3);
            this.tabMappings.Size = new System.Drawing.Size(1107, 176);
            this.tabMappings.TabIndex = 1;
            this.tabMappings.Text = "Mappings";
            this.tabMappings.UseVisualStyleBackColor = true;
            // 
            // cmdJumble
            // 
            this.cmdJumble.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cmdJumble.Location = new System.Drawing.Point(989, 43);
            this.cmdJumble.Name = "cmdJumble";
            this.cmdJumble.Size = new System.Drawing.Size(112, 31);
            this.cmdJumble.TabIndex = 2;
            this.cmdJumble.Text = "&Jumble";
            this.cmdJumble.UseVisualStyleBackColor = true;
            this.cmdJumble.Click += new System.EventHandler(this.cmdJumble_Click);
            // 
            // cmdDefaultMappings
            // 
            this.cmdDefaultMappings.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cmdDefaultMappings.Location = new System.Drawing.Point(989, 6);
            this.cmdDefaultMappings.Name = "cmdDefaultMappings";
            this.cmdDefaultMappings.Size = new System.Drawing.Size(112, 31);
            this.cmdDefaultMappings.TabIndex = 1;
            this.cmdDefaultMappings.Text = "&Defaults";
            this.cmdDefaultMappings.UseVisualStyleBackColor = true;
            this.cmdDefaultMappings.Click += new System.EventHandler(this.cmdDefaultMappings_Click);
            // 
            // lvwMappings
            // 
            this.lvwMappings.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lvwMappings.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colNumber,
            this.colLetter});
            this.lvwMappings.FullRowSelect = true;
            this.lvwMappings.HideSelection = false;
            this.lvwMappings.LabelEdit = true;
            this.lvwMappings.Location = new System.Drawing.Point(3, 3);
            this.lvwMappings.Name = "lvwMappings";
            this.lvwMappings.Size = new System.Drawing.Size(980, 170);
            this.lvwMappings.TabIndex = 0;
            this.lvwMappings.UseCompatibleStateImageBehavior = false;
            this.lvwMappings.View = System.Windows.Forms.View.Details;
            this.lvwMappings.AfterLabelEdit += new System.Windows.Forms.LabelEditEventHandler(this.lvwMappings_AfterLabelEdit);
            // 
            // colNumber
            // 
            this.colNumber.Text = "Number";
            this.colNumber.Width = 148;
            // 
            // colLetter
            // 
            this.colLetter.Text = "Letter";
            this.colLetter.Width = 125;
            // 
            // tabDifficulty
            // 
            this.tabDifficulty.Controls.Add(this.lblMaxDividendValue);
            this.tabDifficulty.Controls.Add(this.txtMaxDividendValue);
            this.tabDifficulty.Controls.Add(this.lblMaxFactorValue);
            this.tabDifficulty.Controls.Add(this.txtMaxFactorValue);
            this.tabDifficulty.Location = new System.Drawing.Point(4, 29);
            this.tabDifficulty.Name = "tabDifficulty";
            this.tabDifficulty.Padding = new System.Windows.Forms.Padding(3);
            this.tabDifficulty.Size = new System.Drawing.Size(1107, 176);
            this.tabDifficulty.TabIndex = 2;
            this.tabDifficulty.Text = "Difficulty";
            this.tabDifficulty.UseVisualStyleBackColor = true;
            // 
            // lblMaxDividendValue
            // 
            this.lblMaxDividendValue.AutoSize = true;
            this.lblMaxDividendValue.Location = new System.Drawing.Point(17, 53);
            this.lblMaxDividendValue.Name = "lblMaxDividendValue";
            this.lblMaxDividendValue.Size = new System.Drawing.Size(186, 20);
            this.lblMaxDividendValue.TabIndex = 2;
            this.lblMaxDividendValue.Text = "Maximum &Dividend Value";
            // 
            // txtMaxDividendValue
            // 
            this.txtMaxDividendValue.Location = new System.Drawing.Point(209, 50);
            this.txtMaxDividendValue.Name = "txtMaxDividendValue";
            this.txtMaxDividendValue.Size = new System.Drawing.Size(124, 26);
            this.txtMaxDividendValue.TabIndex = 3;
            this.txtMaxDividendValue.Validated += new System.EventHandler(this.txtMaxDividendValue_Validated);
            // 
            // lblMaxFactorValue
            // 
            this.lblMaxFactorValue.AutoSize = true;
            this.lblMaxFactorValue.Location = new System.Drawing.Point(32, 21);
            this.lblMaxFactorValue.Name = "lblMaxFactorValue";
            this.lblMaxFactorValue.Size = new System.Drawing.Size(171, 20);
            this.lblMaxFactorValue.TabIndex = 0;
            this.lblMaxFactorValue.Text = "Maximum &Factor Value";
            // 
            // txtMaxFactorValue
            // 
            this.txtMaxFactorValue.Location = new System.Drawing.Point(209, 18);
            this.txtMaxFactorValue.Name = "txtMaxFactorValue";
            this.txtMaxFactorValue.Size = new System.Drawing.Size(124, 26);
            this.txtMaxFactorValue.TabIndex = 1;
            this.txtMaxFactorValue.Validated += new System.EventHandler(this.txtMaxFactorValue_Validated);
            // 
            // cmdCopy
            // 
            this.cmdCopy.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cmdCopy.Location = new System.Drawing.Point(993, 62);
            this.cmdCopy.Name = "cmdCopy";
            this.cmdCopy.Size = new System.Drawing.Size(112, 35);
            this.cmdCopy.TabIndex = 2;
            this.cmdCopy.Text = "&Copy";
            this.cmdCopy.UseVisualStyleBackColor = true;
            this.cmdCopy.Click += new System.EventHandler(this.cmdCopy_Click);
            // 
            // cmdRegenerate
            // 
            this.cmdRegenerate.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cmdRegenerate.Location = new System.Drawing.Point(993, 21);
            this.cmdRegenerate.Name = "cmdRegenerate";
            this.cmdRegenerate.Size = new System.Drawing.Size(112, 35);
            this.cmdRegenerate.TabIndex = 1;
            this.cmdRegenerate.Text = "&Regenerate";
            this.cmdRegenerate.UseVisualStyleBackColor = true;
            this.cmdRegenerate.Click += new System.EventHandler(this.cmdRegenerate_Click);
            // 
            // lblPuzzleOutput
            // 
            this.lblPuzzleOutput.AutoSize = true;
            this.lblPuzzleOutput.Location = new System.Drawing.Point(3, 2);
            this.lblPuzzleOutput.Name = "lblPuzzleOutput";
            this.lblPuzzleOutput.Size = new System.Drawing.Size(178, 20);
            this.lblPuzzleOutput.TabIndex = 0;
            this.lblPuzzleOutput.Text = "Coded Message &Output";
            // 
            // rtfPuzzleOutput
            // 
            this.rtfPuzzleOutput.AcceptsTab = true;
            this.rtfPuzzleOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.rtfPuzzleOutput.Font = new System.Drawing.Font("Calibri", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.rtfPuzzleOutput.Location = new System.Drawing.Point(7, 25);
            this.rtfPuzzleOutput.Name = "rtfPuzzleOutput";
            this.rtfPuzzleOutput.Size = new System.Drawing.Size(980, 455);
            this.rtfPuzzleOutput.TabIndex = 0;
            this.rtfPuzzleOutput.Text = "";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1139, 720);
            this.Controls.Add(this.HorizontalSplitContainer);
            this.Name = "frmMain";
            this.Text = "Maths Cypher";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.frmMain_FormClosed);
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.HorizontalSplitContainer.Panel1.ResumeLayout(false);
            this.HorizontalSplitContainer.Panel2.ResumeLayout(false);
            this.HorizontalSplitContainer.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.HorizontalSplitContainer)).EndInit();
            this.HorizontalSplitContainer.ResumeLayout(false);
            this.TabControl.ResumeLayout(false);
            this.tabCodedMessage.ResumeLayout(false);
            this.tabCodedMessage.PerformLayout();
            this.tabMappings.ResumeLayout(false);
            this.tabDifficulty.ResumeLayout(false);
            this.tabDifficulty.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer HorizontalSplitContainer;
        private System.Windows.Forms.TabControl TabControl;
        private System.Windows.Forms.TabPage tabCodedMessage;
        private System.Windows.Forms.TextBox txtCodedMessageInput;
        private System.Windows.Forms.TabPage tabMappings;
        private System.Windows.Forms.ListView lvwMappings;
        private System.Windows.Forms.ColumnHeader colLetter;
        private System.Windows.Forms.ColumnHeader colNumber;
        private System.Windows.Forms.RichTextBox rtfPuzzleOutput;
        private System.Windows.Forms.Label lblPuzzleOutput;
        private System.Windows.Forms.Button cmdRegenerate;
        private System.Windows.Forms.Button cmdDefaultMappings;
        private System.Windows.Forms.Button cmdJumble;
        private System.Windows.Forms.Button cmdCopy;
        private System.Windows.Forms.TabPage tabDifficulty;
        private System.Windows.Forms.Label lblMaxFactorValue;
        private System.Windows.Forms.TextBox txtMaxFactorValue;
        private System.Windows.Forms.Label lblMaxDividendValue;
        private System.Windows.Forms.TextBox txtMaxDividendValue;
    }
}

