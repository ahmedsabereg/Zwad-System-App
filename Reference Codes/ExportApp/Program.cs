using System;
using System.IO;
using ClosedXML.Excel;

class Program
{
    static void Main()
    {
        string csvPath = @"C:\Users\leork\Desktop\Project\NewData\C#_table.csv";
        string excelPath = @"C:\Users\leork\Desktop\Project\NewData\Donations.xlsx";

        if (!File.Exists(csvPath))
        {
            Console.WriteLine("CSV file not found.");
            return;
        }

        var lines = File.ReadAllLines(csvPath);
        using var workbook = new XLWorkbook();
        var worksheet = workbook.Worksheets.Add("Donations");

        // Write headers
        var headers = lines[0].Split(',');
        for (int i = 0; i < headers.Length; i++)
        {
            worksheet.Cell(1, i + 1).Value = headers[i];
        }

        // Write data rows
        for (int row = 1; row < lines.Length; row++)
        {
            var values = lines[row].Split(',');
            for (int col = 0; col < values.Length; col++)
            {
                worksheet.Cell(row + 1, col + 1).Value = values[col];
            }
        }

        worksheet.Columns().AdjustToContents();
        workbook.SaveAs(excelPath);
        Console.WriteLine("Excel file created: " + excelPath);
    }
}