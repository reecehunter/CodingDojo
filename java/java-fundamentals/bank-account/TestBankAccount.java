public class TestBankAccount {
    public static void main(String[] args) {
        BankAccount bank1 = new BankAccount();
        System.out.println("Total Accounts: "+BankAccount.totalBankAccounts);
        System.out.println("Total $: "+bank1.getCombinedBalance());

        bank1.depositMoney(true, 100.0);
        System.out.println("Total $: "+bank1.getCombinedBalance());

        bank1.depositMoney(false, 50.0);
        System.out.println("Total $: "+bank1.getCombinedBalance());

        bank1.withdrawMoney(false, 50.0);
        System.out.println("Total $: "+bank1.getCombinedBalance());

        bank1.withdrawMoney(true, 100.0);
        System.out.println("Total $: "+bank1.getCombinedBalance());
        
        BankAccount bank2 = new BankAccount();
        System.out.println("Total Accounts: "+BankAccount.totalBankAccounts);
    }
}