using System;

namespace laba56
{
    // Класс для работы с рваным массивом
    public class RaggyArray
    {
        Random rnd = new Random();

        // Поля класса
        private int quantityRows;

        private int[][] raggyArray;

        // Конструктор не заполняет рваный массив
        public RaggyArray(int quantityRows, int[] listLengthRows)
        {
            this.quantityRows = quantityRows;
            raggyArray = new int[quantityRows][];

            for (int r = 0; r < quantityRows; r++) 
            {
                raggyArray[r] = new int[listLengthRows[r]];
            }
        }

        // Заполнение массива вручную
        public void FillInput(int[][] raggyArray)
        {
            this.raggyArray = raggyArray;
        }

        // Заполнение массива с помощью ДСЧ
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

        // Выбор способа заполнения массива
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

        // Возвращает рваный массив
        public int[][] GetRaggyArray()
        {
            return raggyArray;
        }

        // Возвращает количество строк в рваном массиве
        public int GetQuantityRows()
        {
            return quantityRows;
        }

        // Удаление K строк, начиная со строки элементов N
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

        // Проверка на пустоту рваного массива
        public bool IsEmpty()
        {
            return quantityRows == 0;
        }
    }
}

