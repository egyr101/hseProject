using System;

namespace laba56
{
    // Класс для работы со строками
    public class TaskOfStrings
    {
        // Поле класса
        private string stringOfUser;

        // Конструктор полностью создает объект
        public TaskOfStrings(string stringOfUser)
        {
            this.stringOfUser = stringOfUser;
        }

        // Возвращает поле строки
        public string GetString()
        {
            return stringOfUser;
        }

        // Смена первого и последнего слова в строке
        public bool Task()
        {
            // Разделяем строку на массив слов
            string[] stringArray = ToStringArray();
            if (stringArray != null) 
            {
                // Смена слов с помощью промежуточной переменной
                string tmp = char.ToLower(stringArray[0][0]) + stringArray[0].Substring(1) + stringArray[stringArray.Length - 1][stringArray[stringArray.Length - 1].Length-1];
                stringArray[stringArray.Length - 1] = char.ToUpper(stringArray[stringArray.Length - 1][0]) + stringArray[stringArray.Length - 1].Substring(1, stringArray[stringArray.Length - 1].Length - 2);
                stringArray[0] = stringArray[stringArray.Length - 1];
                stringArray[stringArray.Length - 1] = tmp;
                
                stringOfUser = String.Join(" ", stringArray);

                return true;
            }
            return false;
            
        }

        // Разделение строки на массив слов
        private string[] ToStringArray()
        {
            if (stringOfUser.IndexOf(" ") == -1)
            {
                return null;
            }
            return stringOfUser.Split(' ');
        }
    }
}

