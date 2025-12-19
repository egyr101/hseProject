using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba56
{
    public class TaskOfStrings
    {
        private string stringOfUser;
        public TaskOfStrings(string stringOfUser)
        {
            this.stringOfUser = stringOfUser;
        }

        public string GetString()
        {
            return stringOfUser;
        }

        public bool Task()
        {
            string[] stringArray = ToStringArray();
            if (stringArray != null) 
            {
                string tmp = char.ToLower(stringArray[0][0]) + stringArray[0].Substring(1) + stringArray[stringArray.Length - 1][stringArray[stringArray.Length - 1].Length-1];
                stringArray[stringArray.Length - 1] = char.ToUpper(stringArray[stringArray.Length - 1][0]) + stringArray[stringArray.Length - 1].Substring(1, stringArray[stringArray.Length - 1].Length - 2);
                stringArray[0] = stringArray[stringArray.Length - 1];
                stringArray[stringArray.Length - 1] = tmp;

                stringOfUser = String.Join(" ", stringArray);

                return true;
            }
            return false;
            
        }

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
