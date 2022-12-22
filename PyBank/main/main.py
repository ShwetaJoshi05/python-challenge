# Import dependencies
import os
import csv

#Path to collect data from the Resouces folder
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Define PyBank's variables
months = []
profit_losses = []
month_counter = 0
current_month_profit_loss = 0
total_profit_loss = 0
profit_loss_change = 0
previous_month_profit_loss = 0


# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Read the header row first
    #csvheader = next(csvfile)
    #print(f"Header: {csvheader}")

    x = 0
    # Read through each row of data after the header
    for row in csvreader:
        if x == 0:
            x = x +1
            continue

        #increamenting months
        month_counter = month_counter + 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        total_profit_loss = total_profit_loss + current_month_profit_loss

        if (month_counter == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

             # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_losses.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss


    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_losses)    
    average_profit_loss = round(sum_profit_loss/(month_counter - 1),2)

    # greatest and lowest changes in "Profit/Losses" over the entire period
    greatest_profit_loss = max(profit_losses)
    lowest_profit_loss = min(profit_losses)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month = profit_losses.index(greatest_profit_loss)
    lowest_month = profit_losses.index(lowest_profit_loss)

    # Assign best and worst month
    best_month = months[highest_month]
    worst_month = months[lowest_month]

    
# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {month_counter}")
print(f"Total:  ${total_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_profit_loss})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_profit_loss})")

# -->>  Export a text file with the results
budget_file = os.path.join("..", "Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_counter}\n")
    outfile.write(f"Total:  ${total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${greatest_profit_loss})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_profit_loss})\n")







