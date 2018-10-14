using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MathsCypher
{
    public class CodedMessage
    {
        public CodedMessage(
            string messageToEncode,
            Random random,
            Dictionary<char, int> mappings,
            int maxFactorValue,
            int maxDividendValue)
        {
            _messageToEncode = messageToEncode;
            _random = random;
            _mappings = mappings;
            _maxFactorValue = maxFactorValue;
            _maxDividendValue = maxDividendValue;
        }
        
        private Random _random;
        private Dictionary<char, int> _mappings;
        private string _messageToEncode;
        private int _maxFactorValue;
        private int _maxDividendValue;

        public IEnumerable<string> Generate()
        {
            foreach (char character in _messageToEncode.ToUpper())
            {
                yield return (encodeCharacter(character));
            }
        }
        
        private string encodeCharacter(char character)
        {
            if (character == ' ' || character.Equals('\n'))
                return Environment.NewLine;

            if (!_mappings.ContainsKey(character))
                return character + "  ";

            var answer = _mappings[character];

            if (getRandomOperation(answer) == Operation.MULTIPLICATION)
            {
                var multiplication = new Multiplication(answer, _random, _maxFactorValue);
                if (multiplication.Factors != FactorPair.Empty)
                    return multiplication.ToString();
            }

            var division = new Division(answer, _random, _maxDividendValue);
            return division.ToString();
        }

        private enum Operation
        {
            MULTIPLICATION,
            DIVISION
        }

        private Operation getRandomOperation(int answer)
        {
            var factors = answer.GetFactors();
            if (factors.Count <= 2)
                return Operation.DIVISION;

            if (_random.NextDouble() >= 0.5)
                return Operation.MULTIPLICATION;

            return Operation.DIVISION;
        }
    }
}