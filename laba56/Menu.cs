using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    // Класс для менюшек
    public class Menu
    {
        // Поля класса
        private string[] tasks;
        private int quantityOfTasks;

        //Конструктор класса добавляет к задачам номера
        private Menu(string[] tasks)
        {
            this.tasks = new string[tasks.Length];
            
            for (int t = 0; t < tasks.Length; t++)
            {
                this.tasks[t] = $"{t + 1}. " + tasks[t];
            }
            quantityOfTasks = this.tasks.Length;
        }

        // Методы, которые возвращают поля класса

        // Возвращет массив задач
        public string[] GetTasks()
        {
            return tasks;
        }

        // Возвращает количество задач
        public int GetQuantityOfTasks()
        {
            return quantityOfTasks;
        }

        // Создание менюшек, которые используются в зоде программы для взаимодействия с пользователем
        static public Menu menuOfFillArray = new Menu(Messages.menuOfFillArray); // Выбор способа заполнения массива
        static public Menu menuOfFillRow = new Menu(Messages.menuOfFillRow); // Выбор способа заполнения строки элементов
        static public Menu menuOfTasksDouble = new Menu(Messages.menuOfTasksDouble); // Выбор задачи с многомерным массивом
        static public Menu menuOfTasksRaggy = new Menu(Messages.menuOfTasksRaggy); // Выбор задачи с рваным массивом
        static public Menu menuOfTasksString = new Menu(Messages.menuOfTasksString); // Выбор задачи со строкой
    }

}

