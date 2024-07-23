fn main() {
    let mut n = String::new();
    let mut target = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    std::io::stdin().read_line(&mut target).unwrap();
    let n: usize = n.trim().parse().unwrap();
    let target = target.trim().parse().unwrap();

    let mut board = vec![
        vec![0; n]; n
    ];

    let dd:[(isize, isize); 4] = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ];

    let n = n as isize;
    let mut cur = n * n;
    let mut d = 0;
    let mut i = 0;
    let mut j = 0;
    while cur > 0 {
        while (0..n).contains(&i) && (0..n).contains(&j) && board[i as usize][j as usize] == 0 {
            board[i as usize][j as usize] = cur;
            cur -= 1;
            i = i + dd[d].0;
            j = j + dd[d].1;
        }

        i = i - dd[d].0;
        j = j - dd[d].1;
        d += 1;
        d %= 4;
        i = i + dd[d].0;
        j = j + dd[d].1;
    }

    let mut answer = [0; 2];
    for i in 0..n {
        for j in 0..n {
            let cur = board[i as usize][j as usize];
            if cur == target {
                answer[0] = i+1;
                answer[1] = j+1;
            }
            print!("{} ", cur);
        }
        println!();
    }

    println!("{} {}", answer[0], answer[1]);
}