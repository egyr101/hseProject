using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class RaggyArray
    {
        Random rnd = new Random();

        private int quantityRows;

        private int[][] raggyArray;

        public RaggyArray(int quantityRows, int[] listLengthRows)
        {
            this.quantityRows = quantityRows;
            raggyArray = new int[quantityRows][];

            for (int r = 0; r < quantityRows; r++) 
            {
                raggyArray[r] = new int[listLengthRows[r]];
            }
        }

        public void FillInput(int[][] raggyArray)
        {
            this.raggyArray = raggyArray;
        }

        public void FillByRandom()
        {
            for (int r = 0; r < quantityRows; r++)
            {
                for (int l = 0; l < raggyArray[r].Length; l++)
                {
                    raggyArray[r][l] = rnd.Next(-100, 100);
                }
            }
        }

        public void Fill(int numberTask, int[][]? raggy)
        {

            switch (numberTask)
            {
                case 1:
                    FillInput(raggy);
                    break;
                case 2:
                    FillByRandom();
                    break;
            }
        }

        public int[][] GetRaggyArray()
        {
            return raggyArray;
        }

        public int GetQuantityRows()
        {
            return quantityRows;
        }

        public bool DeleteKRowsFromN(int n, int k)
        {
            if (IsEmpty())
            {
                return false;
            }

            int[][] newRaggyArray = new int[quantityRows - k][];

            int quantityElemIsDeleted = 0;
            for (int r = 0; r < quantityRows; r++)
            {
                if (!(r >= n && r < k + n))
                {
                    newRaggyArray[r-quantityElemIsDeleted] = raggyArray[r];
                }
                else
                {
                    quantityElemIsDeleted++;
                }

            }

            raggyArray = newRaggyArray;
            quantityRows -= k;

            return true;
        }

        public bool IsEmpty()
        {
            return quantityRows == 0;
        }
    }
}
