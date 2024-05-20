void transfer(Account from,Account to, int amount){
    synchronized(from){
    synchronized(to){
     from.debit(amount);
     to.credit(amount);
}
}

Functional Issues - Deadlock
As synchronized(from) & synchronized(to) will be working simultaneously both both threads are waiting for the other to release the lock, this will create deadlock situation

Execution Issues - Performance
locks adds overhead. In a high-concurrency scenario with frequent transfers, this can impact performance
