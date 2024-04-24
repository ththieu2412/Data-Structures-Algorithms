def DayConDaiNhat(a, b):
    # Tìm dãy con chung dài nhất bắt đầu từ vị trí i trong a và vị trí j trong b
    def find_longest_common_subsequence(a, b, i, j):
        # Tạo bảng lưu trữ độ dài của dãy con chung dài nhất tại mỗi vị trí
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        
        max_length = 0  # Độ dài của dãy con chung dài nhất
        end_index = 0   # Vị trí kết thúc của dãy con chung dài nhất
        
        # Duyệt qua từng phần tử của a và b
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if a[i - 1] == b[j - 1]:  # Nếu phần tử của a và b giống nhau
                    dp[i][j] = dp[i - 1][j - 1] + 1  # Tăng độ dài dãy con chung lên 1
                    if dp[i][j] > max_length:  # Nếu độ dài mới lớn hơn độ dài hiện tại
                        max_length = dp[i][j]  # Cập nhật độ dài mới
                        end_index = i - 1  # Cập nhật vị trí kết thúc mới
        # Tìm dãy con chung dài nhất bắt đầu từ vị trí end_index
        longest_common_subsequence = a[end_index - max_length + 1: end_index + 1]
        return longest_common_subsequence
    
    # Tìm dãy con chung dài nhất bắt đầu từ mỗi vị trí trong a và b
    longest_subsequence = []
    for i in range(len(a)):
        for j in range(len(b)):
            subsequence = find_longest_common_subsequence(a, b, i, j)
            if len(subsequence) > len(longest_subsequence):
                longest_subsequence = subsequence
    return longest_subsequence
    
    

# Kiểm tra phương thức DayConDauTien
def main():
    a = [6, 9,1, 2, 3, 4, 5,3,2]
    b = [6, 9, 8,1, 2, 3, 4, 5, 6, 7]
    print(DayConDaiNhat(a, b))  # Kết quả: [1, 2, 3, 4, 5]

if __name__ == "__main__":
    main()
