use std::io::{self, BufRead};

fn main() {
    // 표준 입력을 가져오기 위한 핸들
    let stdin = io::stdin();
    let handle = stdin.lock();
    
    // 첫째 줄에 있는 테스트 케이스의 개수 읽기
    let mut lines = handle.lines();
    let t: usize = lines.next().unwrap().unwrap().trim().parse().expect("잘못된 입력");

    for _ in 0..t {
        // 각 테스트 케이스의 첫째 줄에 있는 정수의 개수 읽기
        let n: usize = lines.next().unwrap().unwrap().trim().parse().expect("잘못된 입력");
        
        // 각 테스트 케이스의 둘째 줄에 있는 N개의 정수 읽기
        let numbers: Vec<i32> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|s| s.parse().expect("정수로 변환할 수 없습니다"))
            .collect();
        
        // 최솟값과 최댓값 계산
        let min_value = numbers.iter().cloned().min().unwrap();
        let max_value = numbers.iter().cloned().max().unwrap();
        
        // 결과 출력
        println!("{} {}", min_value, max_value);
    }
}
