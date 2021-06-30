def max_sub_array(arr, k):
    window_sum = 0
    max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # 슬라이팅 윈도위의 범위가 K보다 커진 경우
        if window_end >= (k - 1):
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return max_sum

if __name__ == "__main__":
    print(max_sub_array([2,4,7,10,8,4], 3))