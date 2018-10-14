using System;

namespace MathsCypher
{
    internal class Division
    {
        public readonly int Answer;
        public readonly int Factor1;
        public readonly int Factor2;

        private Random _random;

        public Division(int answer, Random random)
        {
            Answer = answer;
            _random = random;

            Factor1 = _random.Next(2, 5);
            Factor2 = answer * Factor1;
        }

        public override string ToString()
        {
            return string.Format("{0} ÷ {1}   ", Factor1, Factor2);
        }
    }
}