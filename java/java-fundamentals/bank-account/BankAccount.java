public class BankAccount {
    private double checkingBalance;
    private double savingsBalance;
    public static int totalBankAccounts = 0;
    public static double totalMoney = 0.0;

    public BankAccount() {
        totalBankAccounts++;
    }

    public void depositMoney(boolean savings, double amount) {
        if(savings) savingsBalance += amount;
        else checkingBalance += amount;
        totalMoney += amount;
    }

    public void withdrawMoney(boolean savings, double amount) {
        if(savings && savingsBalance - amount >= 0) savingsBalance -= amount;
        else if(!savings && checkingBalance - amount >= 0) checkingBalance -= amount;
        totalMoney -= amount;
    }

    public double getCombinedBalance() {
        return checkingBalance + savingsBalance;
    }

    public double getCheckingBalance() {
        return checkingBalance;
    }

    public double getSavingsBalance() {
        return savingsBalance;
    }
}