using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    // Класс отвечающий за работу с многомерными массивами
    public class DoubleArray
    {
        Random rnd = new Random();
        // Поля класса
        private int quantityRows;
        private int quantityColumns;

        private int[,] table;

        // Конструктор класса, многомерный массив остается пустым после создания объекта класса
        public DoubleArray(int quantityRows, int quantityColumns)
        {
            this.quantityRows = quantityRows;
            this.quantityColumns = quantityColumns;
            table = new int[quantityRows, quantityColumns];
        }

        // Заполнение вручную
        private void FillInput(int[,] table)
        {
            this.table = table;
        }

        // Заполнение с помощью ДСЧ
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

        // Выбор способа заполнения
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

        // Методы, которые возвращают поля, напрямую к полям класса из других классов обращаться нельзя
        
        // Получение количества строк
        public int GetQuantityRows()
        {
            return quantityRows;
        }

        // Получение количества столбцов 
        public int GetQuantityColumns()
        {
            return quantityColumns;
        }

        // Получение многомерного массива
        public int[,] GetTable()
        {
            return table;
        }

        // Добавление строки с начала многомерного массива вручную
        private void AddRowToBeginInput(int[] row)
        {
            int[,] newTable = new int[quantityRows + 1, quantityColumns];

            for (int i = 0; i < quantityColumns; i++)
            {
                newTable[0,i] = row[i];
            }

            Update(newTable);
        }

        // Добавление строки с начала многомерного массива с помощью ДСЧ
        private void AddRowToBeginByRandom()
        {
            int[,] newTable = new int[quantityRows + 1, quantityColumns];

            for (int i = 0; i < quantityColumns; i++)
            {
                newTable[0, i] = rnd.Next(-100,100);
            }

            Update(newTable);
            
        }

         // Выбор способа добавления строки
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

        // Дозаполнение обновленного многомерного массива, элементами из старого массива
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

