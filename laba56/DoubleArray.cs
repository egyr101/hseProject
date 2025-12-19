using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class DoubleArray
    {
        Random rnd = new Random();

        private int quantityRows;
        private int quantityColumns;

        private int[,] table;
        
        public DoubleArray(int quantityRows, int quantityColumns)
        {
            this.quantityRows = quantityRows;
            this.quantityColumns = quantityColumns;
            table = new int[quantityRows, quantityColumns];
        }

        private void FillInput(int[,] table)
        {
            this.table = table;
        }

        private void FillByRandom()
        {
            for (int r = 0; r < quantityRows; r++)
            {
                for (int c = 0; c < quantityColumns; c++)
                {
                    table[r, c] = rnd.Next(-100, 100);
                }
            }
        }

        public void Fill(int numberTask, int[,]? table)
        {
            
            switch (numberTask)
            {
                case 1:
                    FillInput(table);
                    break;
                case 2:
                    FillByRandom();
                    break;
            }
        }

        public int GetQuantityRows()
        {
            return quantityRows;
        }

        public int GetQuantityColumns()
        {
            return quantityColumns;
        }
        public int[,] GetTable()
        {
            return table;
        }

        private void AddRowToBeginInput(int[] row)
        {
            int[,] newTable = new int[quantityRows + 1, quantityColumns];

            for (int i = 0; i < quantityColumns; i++)
            {
                newTable[0,i] = row[i];
            }

            Update(newTable);
        }

        private void AddRowToBeginByRandom()
        {
            int[,] newTable = new int[quantityRows + 1, quantityColumns];

            for (int i = 0; i < quantityColumns; i++)
            {
                newTable[0, i] = rnd.Next(-100,100);
            }

            Update(newTable);
            
        }
        public void AddRowToBegin(int numberOfTask, int[]? row)
        {
            
            switch (numberOfTask)
            {
                case 1:
                    AddRowToBeginInput(row);
                    break;
                case 2:
                    AddRowToBeginByRandom();
                    break;
            }
        }

        private void Update(int[,] newTable)
        {
            quantityRows += 1;

            for (int r = 1; r < quantityRows; r++)
            {
                for (int c = 0; c < quantityColumns; c++)
                {
                    newTable[r, c] = table[r - 1, c];
                }
            }

            table = newTable;
        }
    }
}
