using System;
using System.Text.RegularExpressions;

namespace laba56
{
    public class Input
    {
        // Ввод + проверка числа типа int
        static public int Int(string message)
        {
            bool isCorrectInput = false;

            while (!isCorrectInput)
            {
                Console.Write(message);
                isCorrectInput = int.TryParse(Console.ReadLine(), out int intUser);

                if (isCorrectInput)
                {
                    return intUser;
                }
                else
                {
                    Console.WriteLine(CustomErrors.errorMessageInputInt);
                }
            }
            return 0;
        }

        // Ввод + проверка номера строки N для задачи с рваным массивом
        static public int Int(string message, int lengthArray)
        {
            bool isCorrectInput = false;

            while (!isCorrectInput)
            {
                Console.Write(message);
                isCorrectInput = int.TryParse(Console.ReadLine(), out int intUser);

                isCorrectInput = intUser > 0 && intUser <= lengthArray;

                if (isCorrectInput)
                {
                    return intUser;
                }
                else
                {
                    Console.WriteLine(CustomErrors.errorMessageInputN);
                }
            }
            return 0;
        }

        // Ввод + проверка количества строк N для задачи с рваным массивом
        static public int Int(string message, int lengthArray, int n)
        {
            bool isCorrectInput = false;

            while (!isCorrectInput)
            {
                Console.Write(message);
                isCorrectInput = int.TryParse(Console.ReadLine(), out int intUser);

                isCorrectInput = intUser >= 0 && intUser <= lengthArray && intUser + n <= lengthArray;

                if (isCorrectInput)
                {
                    return intUser;
                }
                else
                {
                    Console.WriteLine(CustomErrors.errorMessageInputK);
                }
            }
            return 0;
        }

        // Ввод + проверка длины массива или номера задачи
        static public int NaturalNumber(string message, string messageError, int? maxNumber)
        {
            bool isCorrectInput = false;

            while (!isCorrectInput)
            {
                Console.Write(message);
                isCorrectInput = int.TryParse(Console.ReadLine(), out int intUser);
                isCorrectInput = maxNumber != null ? intUser > 0 && intUser <= maxNumber : intUser > 0;

                if (isCorrectInput)
                {
                    return intUser;
                }
                else
                {
                    Console.WriteLine(messageError);
                }
            }
            return 0;
        }

        //Ввод + проверка многомерного массива
        static public int[,] DoubleArray(int quantityRows, int quantityColumns)
        {
            int[,] doubleArray = new int[quantityRows, quantityColumns];

            for (int r = 0; r < quantityRows; r++)
            {
                for(int c = 0;  c < quantityColumns; c++)
                {
                    doubleArray[r, c] = Int(Messages.messageInputElemDoubleArray);
                }
            }

            return doubleArray;
        }

        //Ввод + проверка строки элементов в рваном массиве, но подходит также под массив
        static public int[] Array(int length)
        {
            int[] array = new int[length];

            for(int i = 0; i < array.Length; i++)
            {
                array[i] = Int(Messages.messageInputElemRaggyArray);
            }

            return array;
        }

        //Ввод + проверка массива длин строк элементов рваного массива
        static public int[] ArrayLengths(int length)
        {
            int[] array = new int[length];

            for (int i = 0; i < array.Length; i++)
            {
                array[i] = NaturalNumber(Messages.messageInputLengthRow, CustomErrors.errorMessageInputLengthRow, null);
            }

            return array;
        }

        // Ввод + проверка строки
        static public string InputString()
        {
            Regex regex = new Regex(@"[?.,!\-;:]+");

            bool isCorrectInput = false;
            while (!isCorrectInput)
            {
                Console.Write(Messages.messageInputString);
                string stringOfUser= Console.ReadLine();

                MatchCollection matches = regex.Matches(stringOfUser);

                isCorrectInput = true;
                for (int s = 0; s < matches.Count; s++)
                {
                    if (matches[s].Value.Length > 1 && matches[s].Value != "..." && matches[s].Value != "!?" && matches[s].Value != "?!")
                    {
                        isCorrectInput = false;
                        break;
                    }
                }

                if (isCorrectInput)
                {
                    return stringOfUser;
                }
                else
                {
                    Console.WriteLine(CustomErrors.errorMessageInputString);
                }
            }
            return "";
        }
    }
}


