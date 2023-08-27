X_test = [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 8, 14, 15, 15, 15, 15, 15, 15, 12, 10, 14, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 10, 15, 15, 15, 15, 4, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 12, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 6, 0, 8, 15, 15, 15, 15, 15, 12, 0, 2, 15, 15, 15, 15, 15, 12, 0, 0, 9, 13, 14, 14, 11, 3, 0, 8, 15, 15, 15, 15, 15, 15, 10, 1, 0, 0, 1, 0, 0, 0, 7, 15, 15, 15, 15, 15, 15, 15, 15, 13, 9, 6, 5, 6, 8, 12, 15, 15, 15, 15, 14], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 9, 13, 15, 13, 13, 15, 15, 15, 8, 8, 15, 15, 15, 15, 15, 5, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 12, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 11, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 11, 15, 15, 15, 3, 6, 15, 15, 14, 14, 13, 3, 0, 11, 13, 11, 10, 15, 15, 15, 3, 6, 15, 14, 14, 13, 13, 2, 0, 11, 12, 11, 10, 15, 15, 15, 3, 6, 15, 14, 13, 13, 12, 2, 0, 10, 11, 10, 10, 15, 15, 15, 5, 3, 14, 13, 13, 13, 11, 0, 1, 11, 11, 10, 9, 15, 15, 15, 9, 0, 9, 13, 13, 13, 7, 0, 3, 11, 10, 9, 9, 15, 15, 14, 13, 3, 0, 4, 6, 5, 0, 0, 7, 11, 10, 9, 8, 15, 14, 14, 14, 12, 5, 0, 0, 0, 0, 5, 11, 10, 10, 9, 8, 15, 14, 13, 13, 13, 13, 11, 8, 8, 9, 11, 10, 10, 9, 8, 8], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 15, 15, 15, 15, 15, 15, 10, 10, 15, 15, 15, 15, 15, 15, 9, 1, 13, 15, 15, 15, 15, 15, 6, 5, 15, 15, 15, 15, 15, 15, 9, 0, 12, 15, 15, 15, 15, 15, 7, 5, 15, 15, 15, 15, 15, 15, 10, 0, 11, 15, 15, 15, 15, 15, 8, 4, 15, 15, 15, 15, 15, 15, 10, 0, 10, 15, 15, 15, 15, 15, 9, 3, 15, 15, 15, 15, 15, 15, 11, 0, 9, 14, 13, 10, 8, 5, 2, 3, 15, 15, 15, 15, 15, 15, 12, 0, 1, 1, 0, 1, 3, 6, 5, 2, 15, 15, 15, 15, 15, 15, 12, 0, 4, 10, 12, 14, 15, 15, 11, 1, 14, 15, 15, 15, 15, 15, 13, 0, 7, 15, 15, 15, 15, 15, 12, 1, 14, 15, 15, 15, 15, 15, 14, 0, 6, 15, 15, 15, 15, 15, 13, 1, 13, 15, 15, 15, 15, 15, 14, 1, 5, 15, 15, 15, 15, 15, 13, 0, 12, 15, 15, 15, 15, 15, 15, 1, 4, 15, 15, 15, 15, 15, 14, 6, 14, 15, 15, 15, 15, 15, 15, 1, 3, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 11, 10, 14, 15, 15, 15, 15, 15, 15, 13, 15, 15, 15, 15, 15, 15, 4, 0, 11, 15, 15, 15, 15, 15, 13, 1, 11, 15, 15, 15, 15, 15, 5, 0, 10, 15, 15, 15, 15, 15, 13, 0, 10, 15, 15, 15, 15, 15, 5, 0, 10, 15, 15, 15, 15, 15, 14, 0, 10, 15, 15, 15, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 14, 0, 9, 15, 15, 15, 15, 15, 7, 0, 8, 15, 15, 15, 15, 15, 14, 0, 9, 15, 15, 15, 15, 15, 7, 0, 8, 15, 15, 15, 15, 15, 14, 0, 8, 15, 15, 15, 14, 15, 8, 0, 7, 15, 15, 15, 15, 15, 14, 1, 7, 15, 15, 15, 14, 15, 8, 0, 6, 15, 15, 15, 15, 15, 14, 1, 7, 15, 15, 15, 14, 15, 9, 0, 4, 15, 15, 15, 15, 15, 13, 0, 9, 15, 15, 15, 14, 14, 12, 0, 1, 12, 15, 15, 15, 15, 6, 0, 13, 15, 15, 15, 13, 14, 14, 5, 0, 2, 8, 10, 8, 3, 0, 8, 15, 15, 15, 15, 13, 13, 14, 13, 5, 0, 0, 0, 0, 3, 10, 15, 15, 15, 15, 15, 13, 13, 14, 14, 14, 13, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 13, 13, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 7, 3, 2, 2, 4, 9, 14, 15, 15, 15, 15, 15, 15, 15, 12, 1, 1, 6, 8, 7, 4, 0, 3, 14, 15, 15, 15, 15, 15, 15, 4, 1, 13, 15, 15, 15, 15, 9, 0, 6, 15, 15, 15, 15, 15, 14, 1, 5, 15, 15, 15, 15, 15, 15, 4, 4, 15, 15, 15, 15, 15, 15, 3, 1, 12, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 11, 1, 0, 4, 8, 11, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 6, 2, 0, 0, 1, 5, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 9, 5, 0, 0, 8, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 12, 2, 0, 13, 15, 15, 15, 15, 8, 1, 13, 15, 15, 15, 15, 15, 15, 8, 0, 11, 15, 15, 15, 15, 11, 0, 5, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 15, 5, 0, 4, 10, 12, 13, 11, 5, 0, 7, 15, 15, 15, 15, 15, 15, 15, 8, 1, 0, 0, 0, 0, 1, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 12, 11, 10, 12, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 13, 7, 3, 2, 2, 4, 9, 14, 15, 15, 15, 15, 15, 15, 15, 12, 1, 1, 6, 8, 7, 4, 0, 3, 14, 15, 15, 15, 15, 15, 15, 4, 1, 13, 15, 15, 15, 15, 9, 0, 6, 15, 15, 15, 15, 15, 14, 1, 5, 15, 15, 15, 15, 15, 15, 4, 4, 15, 15, 15, 15, 15, 15, 3, 1, 12, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 11, 1, 0, 4, 8, 11, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 6, 2, 0, 0, 1, 5, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 9, 5, 0, 0, 8, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 12, 2, 0, 13, 15, 15, 15, 15, 8, 1, 13, 15, 15, 15, 15, 15, 15, 8, 0, 11, 15, 15, 15, 15, 11, 0, 5, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 15, 5, 0, 4, 10, 12, 13, 11, 5, 0, 7, 15, 15, 15, 15, 15, 15, 15, 8, 1, 0, 0, 0, 0, 1, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 12, 11, 10, 12, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 9, 9, 15, 15, 15, 15, 15, 15, 15, 11, 11, 15, 15, 15, 15, 14, 1, 0, 14, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 14, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 14, 2, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 2, 0, 12, 15, 15, 15, 15, 15, 13, 0, 6, 15, 15, 15, 15, 15, 4, 0, 8, 15, 15, 15, 15, 15, 8, 0, 10, 15, 15, 15, 15, 15, 10, 0, 1, 9, 13, 13, 11, 6, 0, 4, 15, 15, 15, 15, 15, 15, 15, 7, 0, 0, 0, 0, 0, 0, 6, 14, 15, 15, 15, 15, 15, 15, 15, 15, 13, 9, 8, 8, 10, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 8, 14, 15, 15, 15, 15, 15, 15, 12, 10, 14, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 10, 15, 15, 15, 15, 4, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 12, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 6, 0, 8, 15, 15, 15, 15, 15, 12, 0, 2, 15, 15, 15, 15, 15, 12, 0, 0, 9, 13, 14, 14, 11, 3, 0, 8, 15, 15, 15, 15, 15, 15, 10, 1, 0, 0, 1, 0, 0, 0, 7, 15, 15, 15, 15, 15, 15, 15, 15, 13, 9, 6, 5, 6, 8, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 14, 11, 10, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 2, 1, 1, 0, 5, 14, 15, 15, 15, 15, 15, 15, 15, 15, 13, 2, 8, 13, 12, 7, 0, 5, 15, 15, 15, 15, 15, 15, 15, 15, 9, 6, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 15, 15, 15, 7, 7, 15, 15, 15, 15, 11, 2, 12, 15, 15, 15, 15, 15, 15, 15, 9, 2, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 2, 0, 6, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 5, 0, 0, 3, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 6, 0, 0, 7, 15, 15, 15, 15, 15, 15, 15, 14, 10, 15, 15, 15, 15, 13, 2, 0, 11, 15, 15, 15, 15, 15, 15, 13, 1, 14, 15, 15, 15, 15, 11, 0, 7, 15, 15, 15, 15, 15, 15, 15, 2, 8, 15, 15, 15, 15, 13, 0, 5, 15, 15, 15, 15, 15, 15, 15, 9, 0, 8, 14, 15, 15, 6, 0, 8, 15, 14, 14, 15, 15, 15, 15, 15, 6, 0, 1, 3, 2, 0, 2, 13, 15, 14, 13, 15, 15, 15, 15, 15, 15, 11, 5, 2, 2, 5, 13, 15, 15, 14, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 13, 12], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 15, 15, 15, 15, 15, 15, 12, 2, 7, 15, 15, 15, 15, 15, 14, 5, 14, 15, 15, 15, 15, 15, 11, 0, 6, 15, 15, 15, 15, 15, 14, 6, 14, 15, 15, 15, 15, 15, 11, 0, 8, 15, 15, 15, 15, 15, 14, 6, 14, 15, 15, 15, 15, 15, 10, 0, 8, 15, 15, 15, 15, 15, 14, 6, 15, 15, 15, 15, 15, 15, 11, 0, 9, 15, 15, 15, 15, 15, 14, 5, 10, 10, 10, 10, 10, 10, 6, 0, 10, 15, 15, 15, 15, 15, 13, 4, 6, 5, 4, 3, 3, 2, 0, 0, 11, 15, 15, 15, 15, 15, 13, 5, 14, 15, 15, 15, 14, 14, 7, 0, 11, 15, 15, 15, 15, 15, 13, 5, 15, 15, 15, 15, 15, 15, 8, 0, 11, 15, 15, 15, 15, 15, 12, 4, 15, 15, 15, 15, 15, 15, 7, 0, 12, 15, 15, 15, 15, 15, 11, 3, 15, 15, 15, 15, 15, 15, 6, 0, 12, 15, 15, 15, 15, 15, 11, 3, 15, 15, 15, 15, 15, 15, 5, 0, 12, 15, 15, 15, 15, 15, 14, 12, 15, 15, 15, 15, 15, 15, 4, 0, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 6, 14, 15, 15, 15], [15, 15, 15, 15, 15, 14, 13, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 9, 3, 1, 0, 0, 2, 5, 12, 15, 15, 15, 15, 15, 15, 15, 5, 0, 3, 8, 10, 10, 7, 1, 0, 11, 15, 15, 15, 15, 15, 10, 0, 4, 15, 15, 15, 15, 15, 13, 1, 2, 15, 15, 15, 15, 15, 7, 0, 9, 15, 15, 15, 15, 15, 15, 8, 6, 14, 15, 15, 15, 15, 10, 0, 3, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 0, 0, 2, 5, 8, 11, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 11, 6, 2, 0, 0, 0, 0, 5, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 11, 9, 4, 0, 2, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 8, 0, 9, 15, 15, 15, 14, 5, 3, 14, 15, 15, 15, 15, 15, 15, 12, 0, 9, 15, 15, 15, 15, 4, 0, 7, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 12, 1, 0, 4, 9, 11, 11, 8, 3, 0, 9, 15, 15, 15, 15, 15, 15, 12, 4, 0, 0, 0, 0, 0, 4, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 12, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 9, 13, 15, 13, 15, 15, 15, 15, 8, 8, 15, 15, 15, 15, 15, 5, 0, 11, 14, 13, 15, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 15, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 15, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 12, 15, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 15, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 15, 15, 15, 15, 3, 6, 15, 15, 14, 14, 13, 3, 0, 11, 13, 11, 15, 15, 15, 15, 3, 6, 15, 14, 14, 13, 13, 2, 0, 11, 12, 11, 15, 15, 15, 15, 3, 6, 15, 14, 13, 13, 12, 2, 0, 10, 11, 10, 15, 15, 15, 15, 5, 3, 14, 13, 13, 13, 11, 0, 1, 11, 11, 10, 15, 15, 15, 15, 9, 0, 9, 13, 13, 13, 7, 0, 3, 11, 10, 9, 15, 15, 15, 14, 13, 3, 0, 4, 6, 5, 0, 0, 7, 11, 10, 9, 15, 15, 14, 14, 14, 12, 5, 0, 0, 0, 0, 5, 11, 10, 10, 9, 15, 15, 14, 13, 13, 13, 13, 11, 8, 8, 9, 11, 10, 10, 9, 8, 15, 14, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 10, 9, 9, 8], [15, 15, 15, 15, 9, 3, 1, 0, 0, 2, 5, 12, 15, 15, 15, 15, 15, 15, 15, 5, 0, 3, 8, 10, 10, 7, 1, 0, 11, 15, 15, 15, 15, 15, 10, 0, 4, 15, 15, 15, 15, 15, 13, 1, 2, 15, 15, 15, 15, 15, 7, 0, 9, 15, 15, 15, 15, 15, 15, 8, 6, 14, 15, 15, 15, 15, 10, 0, 3, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 0, 0, 2, 5, 8, 11, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 11, 6, 2, 0, 0, 0, 0, 5, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 11, 9, 4, 0, 2, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 8, 0, 9, 15, 15, 15, 14, 5, 3, 14, 15, 15, 15, 15, 15, 15, 12, 0, 9, 15, 15, 15, 15, 4, 0, 7, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 12, 1, 0, 4, 9, 11, 11, 8, 3, 0, 9, 15, 15, 15, 15, 15, 15, 12, 4, 0, 0, 0, 0, 0, 4, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 12, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 14, 13, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 9, 3, 1, 0, 0, 2, 5, 12, 15, 15, 15, 15, 15, 15, 15, 5, 0, 3, 8, 10, 10, 7, 1, 0, 11, 15, 15, 15, 15, 15, 10, 0, 4, 15, 15, 15, 15, 15, 13, 1, 2, 15, 15, 15, 15, 15, 7, 0, 9, 15, 15, 15, 15, 15, 15, 8, 6, 14, 15, 15, 15, 15, 10, 0, 3, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 0, 0, 2, 5, 8, 11, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 11, 6, 2, 0, 0, 0, 0, 5, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 11, 9, 4, 0, 2, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 8, 0, 9, 15, 15, 15, 14, 5, 3, 14, 15, 15, 15, 15, 15, 15, 12, 0, 9, 15, 15, 15, 15, 4, 0, 7, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 12, 1, 0, 4, 9, 11, 11, 8, 3, 0, 9, 15, 15, 15, 15, 15, 15, 12, 4, 0, 0, 0, 0, 0, 4, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 12, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 14, 11, 10, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 2, 1, 1, 0, 5, 14, 15, 15, 15, 15, 15, 15, 15, 15, 13, 2, 8, 13, 12, 7, 0, 5, 15, 15, 15, 15, 15, 15, 15, 15, 9, 6, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 15, 15, 15, 7, 7, 15, 15, 15, 15, 11, 2, 12, 15, 15, 15, 15, 15, 15, 15, 9, 2, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 2, 0, 6, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 5, 0, 0, 3, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 6, 0, 0, 7, 15, 15, 15, 15, 15, 15, 15, 14, 10, 15, 15, 15, 15, 13, 2, 0, 11, 15, 15, 15, 14, 15, 15, 13, 1, 14, 15, 15, 15, 15, 11, 0, 7, 15, 15, 15, 14, 15, 15, 15, 2, 8, 15, 15, 15, 15, 13, 0, 5, 15, 15, 15, 14, 15, 15, 15, 9, 0, 8, 14, 15, 15, 6, 0, 8, 15, 14, 14, 13, 15, 15, 15, 15, 6, 0, 1, 3, 2, 0, 2, 13, 15, 14, 13, 13, 15, 15, 15, 15, 15, 11, 5, 2, 2, 5, 13, 15, 15, 14, 13, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 13, 12, 11, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 11, 10, 14, 15, 15, 15, 15, 15, 15, 13, 15, 15, 15, 15, 15, 15, 4, 0, 11, 15, 15, 15, 15, 15, 13, 1, 11, 15, 15, 15, 15, 15, 5, 0, 10, 15, 15, 15, 15, 15, 13, 0, 10, 15, 15, 15, 15, 15, 5, 0, 10, 15, 15, 15, 15, 15, 14, 0, 10, 15, 15, 15, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 14, 0, 9, 15, 15, 15, 15, 15, 7, 0, 8, 15, 15, 15, 15, 15, 14, 0, 9, 15, 15, 15, 15, 15, 7, 0, 8, 15, 15, 15, 15, 15, 14, 0, 8, 15, 15, 15, 14, 15, 8, 0, 7, 15, 15, 15, 15, 15, 14, 1, 7, 15, 15, 15, 14, 15, 8, 0, 6, 15, 15, 15, 15, 15, 14, 1, 7, 15, 15, 15, 14, 15, 9, 0, 4, 15, 15, 15, 15, 15, 13, 0, 9, 15, 15, 15, 14, 14, 12, 0, 1, 12, 15, 15, 15, 15, 6, 0, 13, 15, 15, 15, 13, 14, 14, 5, 0, 2, 8, 10, 8, 3, 0, 8, 15, 15, 15, 15, 13, 13, 14, 13, 5, 0, 0, 0, 0, 3, 10, 15, 15, 15, 15, 15, 13, 13, 14, 14, 14, 13, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 13, 13, 13, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 7, 3, 2, 2, 4, 9, 14, 15, 15, 15, 15, 15, 15, 15, 12, 1, 1, 6, 8, 7, 4, 0, 3, 14, 15, 15, 15, 15, 15, 15, 4, 1, 13, 15, 15, 15, 15, 9, 0, 6, 15, 15, 15, 15, 15, 14, 1, 5, 15, 15, 15, 15, 15, 15, 4, 4, 15, 15, 15, 15, 15, 15, 3, 1, 12, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 11, 1, 0, 4, 8, 11, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 6, 2, 0, 0, 1, 5, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 9, 5, 0, 0, 8, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 12, 2, 0, 13, 15, 15, 15, 15, 8, 1, 13, 15, 15, 15, 15, 15, 15, 8, 0, 11, 15, 15, 15, 15, 11, 0, 5, 15, 15, 15, 15, 15, 15, 5, 0, 13, 15, 15, 15, 15, 15, 5, 0, 4, 10, 12, 13, 11, 5, 0, 7, 15, 15, 15, 15, 15, 15, 15, 8, 1, 0, 0, 0, 0, 1, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 12, 11, 10, 12, 14, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 12, 8, 7, 8, 11, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 4, 0, 0, 2, 1, 0, 4, 14, 15, 15, 15, 15, 15, 15, 15, 5, 0, 8, 14, 15, 15, 11, 1, 5, 15, 15, 15, 15, 15, 15, 13, 0, 3, 15, 15, 15, 15, 15, 9, 3, 14, 15, 15, 15, 15, 15, 14, 1, 2, 14, 15, 15, 15, 15, 15, 14, 15, 15, 15, 15, 15, 15, 15, 7, 0, 2, 7, 10, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 8, 2, 0, 0, 0, 1, 5, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 12, 10, 8, 5, 1, 1, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 1, 7, 15, 15, 15, 15, 15, 14, 8, 10, 15, 15, 15, 15, 15, 15, 3, 7, 15, 15, 15, 15, 15, 13, 0, 1, 14, 15, 15, 15, 15, 11, 0, 11, 15, 15, 15, 15, 15, 15, 6, 0, 3, 9, 11, 10, 6, 0, 6, 15, 15, 15, 15, 15, 15, 15, 14, 6, 0, 0, 0, 0, 2, 9, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 11, 11, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 5, 12, 15, 15, 15, 15, 15, 15, 15, 11, 3, 4, 14, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 9, 0, 0, 13, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 9, 0, 1, 13, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 9, 0, 1, 13, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 9, 0, 1, 14, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 9, 0, 1, 14, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 8, 0, 1, 14, 15, 15, 6, 0, 9, 15, 15, 15, 15, 15, 15, 15, 8, 0, 1, 14, 15, 15, 6, 0, 8, 15, 15, 15, 15, 15, 15, 15, 8, 0, 1, 14, 15, 15, 7, 0, 6, 15, 15, 15, 15, 15, 15, 15, 6, 0, 2, 14, 15, 15, 10, 0, 2, 14, 15, 15, 15, 15, 15, 14, 2, 0, 4, 15, 15, 15, 14, 3, 0, 3, 11, 14, 14, 14, 12, 5, 0, 0, 10, 15, 14, 15, 15, 13, 4, 0, 0, 1, 2, 2, 0, 0, 0, 7, 14, 14, 14, 15, 15, 15, 14, 10, 6, 3, 2, 2, 3, 5, 10, 14, 14, 14, 13, 15, 14, 14, 14, 15, 15, 14, 13, 13, 14, 15, 14, 14, 13, 13, 13], [15, 15, 15, 8, 8, 15, 15, 15, 15, 15, 5, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 13, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 15, 4, 0, 11, 14, 12, 12, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 11, 15, 15, 15, 4, 6, 15, 15, 15, 15, 14, 3, 0, 11, 13, 12, 11, 15, 15, 15, 3, 6, 15, 15, 14, 14, 13, 3, 0, 11, 13, 11, 10, 15, 15, 15, 3, 6, 15, 14, 14, 13, 13, 2, 0, 11, 12, 11, 10, 15, 15, 15, 3, 6, 15, 14, 13, 13, 12, 2, 0, 10, 11, 10, 10, 15, 15, 15, 5, 3, 14, 13, 13, 13, 11, 0, 1, 11, 11, 10, 9, 15, 15, 15, 9, 0, 9, 13, 13, 13, 7, 0, 3, 11, 10, 9, 9, 15, 15, 14, 13, 3, 0, 4, 6, 5, 0, 0, 7, 11, 10, 9, 8, 15, 14, 14, 14, 12, 5, 0, 0, 0, 0, 5, 11, 10, 10, 9, 8, 15, 14, 13, 13, 13, 13, 11, 8, 8, 9, 11, 10, 10, 9, 8, 8, 14, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 10, 9, 9, 8, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 12, 15, 15, 15, 15, 15, 15, 12, 2, 7, 15, 15, 15, 15, 15, 14, 5, 14, 15, 15, 15, 15, 15, 11, 0, 6, 15, 15, 15, 15, 15, 14, 6, 14, 15, 15, 15, 15, 15, 11, 0, 8, 15, 15, 15, 15, 15, 14, 6, 14, 15, 15, 15, 15, 15, 10, 0, 8, 15, 15, 15, 15, 15, 14, 6, 15, 15, 15, 15, 15, 15, 11, 0, 9, 15, 15, 15, 15, 15, 14, 5, 10, 10, 10, 10, 10, 10, 6, 0, 10, 15, 15, 15, 15, 15, 13, 4, 6, 5, 4, 3, 3, 2, 0, 0, 11, 15, 15, 15, 15, 15, 13, 5, 14, 15, 15, 15, 14, 14, 7, 0, 11, 15, 15, 15, 15, 15, 13, 5, 15, 15, 15, 15, 15, 15, 8, 0, 11, 15, 15, 15, 15, 15, 12, 4, 15, 15, 15, 15, 15, 15, 7, 0, 12, 15, 15, 15, 15, 15, 11, 3, 15, 15, 15, 15, 15, 15, 6, 0, 12, 15, 15, 15, 15, 15, 11, 3, 15, 15, 15, 15, 15, 15, 5, 0, 12, 15, 15, 15, 15, 15, 14, 12, 15, 15, 15, 15, 15, 15, 4, 0, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 6, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 8, 14, 15, 15, 15, 15, 15, 15, 12, 10, 14, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 10, 15, 15, 15, 15, 4, 0, 13, 15, 15, 15, 15, 15, 15, 7, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 6, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 11, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 5, 0, 12, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 4, 0, 12, 15, 15, 15, 15, 15, 15, 3, 0, 13, 15, 15, 15, 15, 6, 0, 8, 15, 15, 15, 15, 15, 12, 0, 2, 15, 15, 15, 15, 15, 12, 0, 0, 9, 13, 14, 14, 11, 3, 0, 8, 15, 15, 15, 15, 15, 15, 10, 1, 0, 0, 1, 0, 0, 0, 7, 15, 15, 15, 15, 15, 15, 15, 15, 13, 9, 6, 5, 6, 8, 12, 15, 15, 15, 15, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 9, 9, 15, 15, 15, 15, 15, 15, 15, 11, 11, 15, 15, 15, 15, 14, 1, 0, 14, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 14, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 15, 2, 3, 15, 15, 15, 15, 14, 1, 1, 13, 15, 15, 15, 15, 15, 14, 2, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 1, 0, 13, 15, 15, 15, 15, 15, 14, 1, 4, 15, 15, 15, 15, 14, 2, 0, 12, 15, 15, 15, 15, 15, 13, 0, 6, 15, 15, 15, 15, 15, 4, 0, 8, 15, 15, 15, 15, 15, 8, 0, 10, 15, 15, 15, 15, 15, 10, 0, 1, 9, 13, 13, 11, 6, 0, 4, 15, 15, 15, 15, 15, 15, 15, 7, 0, 0, 0, 0, 0, 0, 6, 14, 15, 15, 15, 15, 15, 15, 15, 15, 13, 9, 8, 8, 10, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]]