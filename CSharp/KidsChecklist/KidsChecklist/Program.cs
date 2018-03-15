using KidsCheckList.Properties;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KidsCheckList
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            
            if (isDebugParameterPassed(args) || isBeforeSchool(DateTime.Now))
                Application.Run(new frmMain());
        }

        private static bool isDebugParameterPassed(string[] args)
        {
            return args.Contains("/debug");
        }

        private static bool isBeforeSchool(DateTime time)
        {
            if (time.DayOfWeek == DayOfWeek.Saturday || time.DayOfWeek == DayOfWeek.Sunday)
                return Settings.Default.LaunchOnWeekends;

            return time.Hour < Settings.Default.LaunchBeforeHour;
        }
    }
}
