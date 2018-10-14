using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MathsCypher
{
    public static class Extensions
    {
        public static void AppendText(this RichTextBox textBox, string text, Color colour)
        {
            textBox.SelectionStart = textBox.TextLength;
            textBox.SelectionLength = 0;

            textBox.SelectionColor = colour;
            textBox.AppendText(text);
            textBox.SelectionColor = textBox.ForeColor;
        }

        public static void AppendText(this RichTextBox textBox, string text, Font font)
        {
            textBox.SelectionStart = textBox.TextLength;
            textBox.SelectionLength = 0;

            textBox.SelectionFont = font;
            textBox.AppendText(text);
            textBox.SelectionFont = textBox.Font;
        }

        public static Dictionary<TKey, TValue> Shuffle<TKey, TValue>(
            this Dictionary<TKey, TValue> source)
        {
            Random random = new Random();
            return source.OrderBy(x => random.Next())
               .ToDictionary(item => item.Key, item => item.Value);
        }

        public static List<TValue> Shuffle<TValue>(this List<TValue> source)
        {
            Random random = new Random();
            return source.OrderBy(x => random.Next())
               .ToList();
        }

        public static List<int> GetFactors(this int number)
        {
            List<int> factors = new List<int>();
            int max = (int)Math.Sqrt(number);  //round down
            for (int factor = 1; factor <= max; ++factor)
            { //test from 1 to the square root, or the int below it, inclusive.
                if (number % factor == 0)
                {
                    factors.Add(factor);
                    if (factor != number / factor)
                    { // Don't add the square root twice!  Thanks Jon
                        factors.Add(number / factor);
                    }
                }
            }
            return factors;
        }
    }
}
