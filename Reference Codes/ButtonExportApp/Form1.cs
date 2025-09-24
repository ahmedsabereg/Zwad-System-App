using System;
using System.IO;
using System.Windows.Forms;
using ClosedXML.Excel;

namespace ButtonExportApp
{
    public partial class Form1 : Form
    {
        private Button submitButton;

        public Form1()
        {
            InitializeComponent();

            // Create and add the Submit button
            submitButton = new Button
            {
                Text = "Submit",
                Width = 100,
                Height = 40,
                Top = 30,
                Left = 30
            };
            submitButton.Click += SubmitButton_Click;
            Controls.Add(submitButton);

            // Optional: Set form properties
            this.Text = "CSV to Excel Exporter";
            this.Width = 200;
            this.Height = 120;
        }

        private void SubmitButton_Click(object sender, EventArgs e)
        {
            string csvPath = @"C:\Users\leork\Desktop\Project\Codes\C#_table.csv";
            string excelPath = @"C:\Users\leork\Desktop\Project\Codes\Donations.xlsx";

            if (!File.Exists(csvPath))
            {
                MessageBox.Show("CSV file not found.");
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
            MessageBox.Show("Excel file created: " + excelPath);
        }
    }
}