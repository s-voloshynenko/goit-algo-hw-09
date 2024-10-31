### HM 09 Greedy and Dynamic

#### Результати виконання

```
Amount: 113
Average search time of 'find_coins_greedy' over 10 runs is 0.000001 secs.
Result: {50: 2, 10: 1, 2: 1, 1: 1}
Average search time of 'find_min_coins' over 10 runs is 0.000036 secs.
Result: {1: 1, 2: 1, 10: 1, 50: 2}

Amount: 616
Average search time of 'find_coins_greedy' over 10 runs is 0.000000 secs.
Result: {50: 12, 10: 1, 5: 1, 1: 1}
Average search time of 'find_min_coins' over 10 runs is 0.000232 secs.
Result: {1: 1, 5: 1, 10: 1, 50: 12}

Amount: 10012
Average search time of 'find_coins_greedy' over 10 runs is 0.000000 secs.
Result: {50: 200, 10: 1, 2: 1}
Average search time of 'find_min_coins' over 10 runs is 0.003316 secs.
Result: {2: 1, 10: 1, 50: 200}
```

#### Greedy

Швидший за динамічний але не гарантує мінімальну кількість монет для будь-якого набору монет. Часов складніть `O(n)`, n - кількість номіналів монет.
За результатами тесту бачимо як він випереджає динамічний алгоритм за часом.

#### Dynamic

Повільніший за жадібний але гарантує мінімальну кількість монет для будь-якого набору номіналу. Часова складніть `O(n * m)`, n - кількість номіналів, m - сума в залишку.

При великих сумах, динамічний алгоритм буде значно програвати жадібному але зберігаючи свою ефективність в кількості номіналів.
