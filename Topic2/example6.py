# 하노이의 탑
# : 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것이다.
#   - 한 번에 하나의 원판만 옮길 수 있다.
#   - 큰 원판이 작은 원판 위에 있어서는 안 된다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case : 옮길 원판이 없으면 부분 문제를 나누지 않고 함수를 끝낸다
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg

        # 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)

        # 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)

        # 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)


hanoi(3, 1, 3)