namespace laba56
{
    public class Program
    {
        static void Main(string[] args)
        {
            DoubleArray table = new DoubleArray(Input.NaturalNumber(Messages.messageInputQuantityRowsDouble, CustomErrors.errorMessageInputQuantityRowsDouble, null), Input.NaturalNumber(Messages.messageInputQuantityColumnsDouble, CustomErrors.errorMessageInputQuantityColumnsDouble, null));
            Messages.PrintMenu(Menu.menuOfFillArray);
            int numberOfMethod = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, Menu.menuOfFillArray.GetQuantityOfTasks());
            if (numberOfMethod == 2)
            {
                table.Fill(numberOfMethod, null);
            }
            else
            {
                table.Fill(numberOfMethod, Input.DoubleArray(table.GetQuantityRows(), table.GetQuantityColumns()));
            }

            bool isExited = false;
            while (!isExited)
            {
                Messages.PrintMenu(Menu.menuOfTasksDouble);

                int numberOftask = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, Menu.menuOfTasksDouble.GetQuantityOfTasks());

                switch (numberOftask)
                {
                    case 1:
                        table = new DoubleArray(Input.NaturalNumber(Messages.messageInputQuantityRowsDouble, CustomErrors.errorMessageInputQuantityRowsDouble, null), Input.NaturalNumber(Messages.messageInputQuantityColumnsDouble, CustomErrors.errorMessageInputQuantityColumnsDouble, null));
                        Messages.PrintMenu(Menu.menuOfFillArray);
                        numberOfMethod = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, Menu.menuOfFillArray.GetQuantityOfTasks());

                        if (numberOfMethod == 2)
                        {
                            table.Fill(numberOfMethod, null);
                        }
                        else
                        {
                            int[,] tmpTable = new int[table.GetQuantityRows(), table.GetQuantityColumns()];
                            table.Fill(numberOfMethod, tmpTable);
                        }
                        break;
                    case 2:
                        Messages.PrintArray(table);
                        break;
                    case 3:
                        Messages.PrintMenu(Menu.menuOfFillRow);
                        numberOfMethod = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, 2);
                        table.AddRowToBegin(numberOfMethod, Input.Array(table.GetQuantityColumns()));
                        break;
                    case 4:
                        isExited = true;
                        break;
                }
            }

            isExited = false;

            int quantityRows = Input.NaturalNumber(Messages.messageInputQuantityRowsRaggy, CustomErrors.errorMessageInputQuantityRowsRaggy, null);
            int[] listLengthRows = Input.ArrayLengths(quantityRows);
            RaggyArray raggy = new RaggyArray(quantityRows, listLengthRows);

            Messages.PrintMenu(Menu.menuOfFillArray);
            numberOfMethod = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, 2);
            if(numberOfMethod == 2)
            {
                raggy.Fill(numberOfMethod, null);
            }
            else
            {
                int[][] tmpRaggy = new int[table.GetQuantityRows()][];

                for (int i = 0; i < listLengthRows.Length; i++)
                {
                    tmpRaggy[i] = Input.Array(listLengthRows[i]);
                }
                raggy.Fill(numberOfMethod, tmpRaggy);
            }

            while (!isExited)
            {
                Messages.PrintMenu(Menu.menuOfTasksRaggy);

                int numberOftask = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, Menu.menuOfTasksRaggy.GetQuantityOfTasks());

                switch (numberOftask)
                {
                    case 1:
                        quantityRows = Input.NaturalNumber(Messages.messageInputQuantityRowsRaggy, CustomErrors.errorMessageInputQuantityRowsRaggy, null);
                        listLengthRows = Input.ArrayLengths(quantityRows);
                        raggy = new RaggyArray(quantityRows, listLengthRows);

                        Messages.PrintMenu(Menu.menuOfFillArray);
                        numberOfMethod = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, 2);
                        if (numberOfMethod == 2)
                        {
                            raggy.Fill(numberOfMethod, null);
                        }
                        else
                        {
                            int[][] tmpRaggy = new int[table.GetQuantityRows()][];

                            for (int i = 0; i < listLengthRows.Length; i++)
                            {
                                tmpRaggy[i] = Input.Array(listLengthRows[i]);
                            }
                            raggy.Fill(numberOfMethod, tmpRaggy);
                        }
                        break;
                    case 2:
                        Messages.PrintArray(raggy);
                        break;
                    case 3:
                        int n = Input.Int(Messages.messageInputN, raggy.GetQuantityRows()) - 1;
                        int k = Input.Int(Messages.messageInputK, raggy.GetQuantityRows(), n);

                        if (!(raggy.DeleteKRowsFromN(n, k)))
                        {
                            Console.WriteLine(CustomErrors.errorArrayIsEmpty);
                        }
                        break;
                    case 4:
                        isExited = true;
                        break;
                }
            }
            isExited = false;

            TaskOfStrings stringOfUser = new TaskOfStrings(Input.InputString());

            while (!isExited) 
            {
                Messages.PrintMenu(Menu.menuOfTasksString);

                int numberOftask = Input.NaturalNumber(Messages.messageInputNumberTask, CustomErrors.errorMessageInputNumberTask, Menu.menuOfTasksString.GetQuantityOfTasks());

                switch (numberOftask) 
                {
                    case 1:
                        stringOfUser = new TaskOfStrings(Input.InputString());
                        break;
                    case 2:
                        Console.WriteLine(stringOfUser.GetString());
                        break;
                    case 3:
                        if (!stringOfUser.Task())
                        {
                            Console.WriteLine(CustomErrors.errorMessageStringHasOneWord);
                        }
                        ;
                        break;
                    case 4:
                        isExited = true;
                        break;
                }
            }
        }
    }
}
