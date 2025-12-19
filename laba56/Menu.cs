using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class Menu
    {
        private string[] tasks;
        private int quantityOfTasks;

        private Menu(string[] tasks)
        {
            this.tasks = new string[tasks.Length];
            
            for (int t = 0; t < tasks.Length; t++)
            {
                this.tasks[t] = $"{t + 1}. " + tasks[t];
            }
            quantityOfTasks = this.tasks.Length;
        }

        public string[] GetTasks()
        {
            return tasks;
        }

        public int GetQuantityOfTasks()
        {
            return quantityOfTasks;
        }

        static public Menu menuOfFillArray = new Menu(Messages.menuOfFillArray);
        static public Menu menuOfFillRow = new Menu(Messages.menuOfFillRow);
        static public Menu menuOfTasksDouble = new Menu(Messages.menuOfTasksDouble);
        static public Menu menuOfTasksRaggy = new Menu(Messages.menuOfTasksRaggy);
        static public Menu menuOfTasksString = new Menu(Messages.menuOfTasksString);
    }

}
