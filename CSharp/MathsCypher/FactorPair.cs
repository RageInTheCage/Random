namespace MathsCypher
{
    public class FactorPair
    {
        public readonly int Factor1;
        public readonly int Factor2;

        public static FactorPair Empty = new FactorPair(0, 0);

        public FactorPair(int factor1, int factor2)
        {
            Factor1 = factor1;
            Factor2 = factor2;
        }
    }
}