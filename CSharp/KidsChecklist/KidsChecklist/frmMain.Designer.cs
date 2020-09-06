namespace KidsCheckList
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
            this.components = new System.ComponentModel.Container();
            this.picNoodle = new System.Windows.Forms.PictureBox();
            this.bindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.lvwCheckList = new System.Windows.Forms.ListView();
            this.lblNoodleSpeech = new System.Windows.Forms.Label();
            this.cmdYesImSure = new System.Windows.Forms.Button();
            this.tmrCloseForm = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picNoodle)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            this.SuspendLayout();
            // 
            // picNoodle
            // 
            this.picNoodle.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.picNoodle.InitialImage = null;
            this.picNoodle.Location = new System.Drawing.Point(18, 18);
            this.picNoodle.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.picNoodle.Name = "picNoodle";
            this.picNoodle.Size = new System.Drawing.Size(390, 346);
            this.picNoodle.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picNoodle.TabIndex = 0;
            this.picNoodle.TabStop = false;
            // 
            // lvwCheckList
            // 
            this.lvwCheckList.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.lvwCheckList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(164)))), ((int)(((byte)(97)))), ((int)(((byte)(76)))));
            this.lvwCheckList.CheckBoxes = true;
            this.lvwCheckList.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lvwCheckList.ForeColor = System.Drawing.SystemColors.Window;
            this.lvwCheckList.Location = new System.Drawing.Point(248, 277);
            this.lvwCheckList.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.lvwCheckList.Name = "lvwCheckList";
            this.lvwCheckList.Size = new System.Drawing.Size(165, 104);
            this.lvwCheckList.TabIndex = 2;
            this.lvwCheckList.UseCompatibleStateImageBehavior = false;
            this.lvwCheckList.View = System.Windows.Forms.View.List;
            this.lvwCheckList.ItemChecked += new System.Windows.Forms.ItemCheckedEventHandler(this.lvwCheckList_ItemChecked);
            // 
            // lblNoodleSpeech
            // 
            this.lblNoodleSpeech.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.lblNoodleSpeech.AutoSize = true;
            this.lblNoodleSpeech.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNoodleSpeech.ForeColor = System.Drawing.Color.AliceBlue;
            this.lblNoodleSpeech.Location = new System.Drawing.Point(116, 277);
            this.lblNoodleSpeech.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblNoodleSpeech.Name = "lblNoodleSpeech";
            this.lblNoodleSpeech.Size = new System.Drawing.Size(236, 29);
            this.lblNoodleSpeech.TabIndex = 3;
            this.lblNoodleSpeech.Text = "Hey Tom, have you...";
            this.lblNoodleSpeech.TextAlign = System.Drawing.ContentAlignment.TopRight;
            // 
            // cmdYesImSure
            // 
            this.cmdYesImSure.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.cmdYesImSure.Location = new System.Drawing.Point(126, 348);
            this.cmdYesImSure.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.cmdYesImSure.Name = "cmdYesImSure";
            this.cmdYesImSure.Size = new System.Drawing.Size(112, 35);
            this.cmdYesImSure.TabIndex = 4;
            this.cmdYesImSure.Text = "&Yes";
            this.cmdYesImSure.UseVisualStyleBackColor = true;
            this.cmdYesImSure.Visible = false;
            this.cmdYesImSure.Click += new System.EventHandler(this.cmdYesImSure_Click);
            // 
            // tmrCloseForm
            // 
            this.tmrCloseForm.Interval = 2000;
            this.tmrCloseForm.Tick += new System.EventHandler(this.tmrCloseForm_Tick);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(125)))), ((int)(((byte)(82)))), ((int)(((byte)(57)))));
            this.ClientSize = new System.Drawing.Size(426, 402);
            this.Controls.Add(this.cmdYesImSure);
            this.Controls.Add(this.lblNoodleSpeech);
            this.Controls.Add(this.lvwCheckList);
            this.Controls.Add(this.picNoodle);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.MinimizeBox = false;
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Kids Checklist";
            this.TopMost = true;
            ((System.ComponentModel.ISupportInitialize)(this.picNoodle)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picNoodle;
        private System.Windows.Forms.BindingSource bindingSource1;
        private System.Windows.Forms.ListView lvwCheckList;
        private System.Windows.Forms.Label lblNoodleSpeech;
        private System.Windows.Forms.Button cmdYesImSure;
        private System.Windows.Forms.Timer tmrCloseForm;
    }
}

