using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class Messages
    {
        // Сообщения, которые могут выводится пользователю в ходе программы
        static public string[] menuOfFillArray = { "Заполнить массив с помощью ручного ввода", "Заполнить массив с помощью ДСЧ" };
        static public string[] menuOfFillRow = { "Заполнить строку с помощью ручного ввода", "Заполнить строку с помощью ДСЧ" };
        static public string[] menuOfTasksDouble = { "Создать двумерный массив", "Вывести двумерный массив", "Добавить строку в начало двумерного массива", "Выход" };
        static public string[] menuOfTasksRaggy = { "Создать рваный массив", "Вывести рваный массив", "Удалить K строк, начиная со строки с номером N", "Выход" };
        static public string[] menuOfTasksString = { "Создать строку", "Вывести строку", "Поменять местами первое и последнее слово в строке", "Выход"};
        public const string messageInputNumberTask= "Введите номер задачи: ";

        public const string messageInputElemDoubleArray = "Введите элемент двумерного массива: ";
        public const string messageInputElemRowDoubleArray = "Введите элемент строки двумерного массива: ";
        public const string messageInputQuantityRowsDouble = "Введите количество строк в двумерном массиве: ";
        public const string messageInputQuantityColumnsDouble = "Введите количество столбцов в двумерном массиве: ";

        public const string messageInputQuantityRowsRaggy = "Введите количество строк в рваном массиве: ";
        public const string messageInputLengthRow = "Введите длину строки в рваном массиве: ";
        public const string messageInputElemRaggyArray = "Введите элемент рваного массива: ";
        public const string messageInputN = "Введите номер строки, начиная с которой вы хотите удалить часть массива: ";
        public const string messageInputK = "Введите количество строк, которое вы хотите удалить: ";

        public const string messageInputString = "Введите строку (в строке не должно быть двух или нескольких подряд стоящих знаков препинания(исключения - !?, ?!)): ";

        // Вывод менюшки
        static public void PrintMenu(Menu menu)
        {

            foreach(string task in menu.GetTasks())
            {
                Console.WriteLine(task);
            }
        }

        // Вывод многомерного массива
        static public void PrintArray(DoubleArray doubleArray)
        {
            int[,] array = doubleArray.GetTable();
            for (int r = 0; r < doubleArray.GetQuantityRows(); r++)
            {
                for (int c = 0; c < doubleArray.GetQuantityColumns(); c++)
                {
                    Console.Write(array[r,c] + " ");
                }

                Console.WriteLine();
            }
        }

        // Вывод рваного массива
        static public void PrintArray(RaggyArray raggyArray)
        {
            int[][] array = raggyArray.GetRaggyArray();
            for (int r = 0; r < raggyArray.GetQuantityRows(); r++)
            {
                for (int c = 0; c < array[r].Length; c++)
                {
                    Console.Write(array[r][c] + " ");
                }

                Console.WriteLine();
            }
        }

        
    }
}

