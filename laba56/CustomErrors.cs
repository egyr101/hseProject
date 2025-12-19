using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class CustomErrors
    {
        public const string errorMessageInputNumberTask = "Нет задачи с таким номером";

        public const string errorArrayIsEmpty = "Рваный массив пустой! Создайте новый массив";

        public const string errorMessageInputInt = "Введена строка или число не типа int!";

        public const string errorMessageInputQuantityColumnsDouble = "Длина столбца двумерного массива должна быть натуральным числом!";
        public const string errorMessageInputQuantityRowsDouble = "Длина строки двумерного массива должна быть натуральным числом!";

        public const string errorMessageInputLengthRow = "Длина строки рваного массива должна быть натуральным числом!";
        public const string errorMessageInputQuantityRowsRaggy = "Количество строк рваного массива должно быть натуральным числом!";
        public const string errorMessageInputN = "В рваном массиве нет строки с таким номером!";
        public const string errorMessageInputK = "В рваном массиве нет такого количества строк!";

        public const string errorMessageInputString = "Введена некорректная строка!";
        public const string errorMessageStringHasOneWord = "Операция невозможна, так как в строке только одно слово!";
    }
}
