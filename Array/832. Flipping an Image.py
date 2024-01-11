class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i]=image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image
        
'''for row in image:
		l = 0 
		r = len(row)-1

		while l <= r:
			row[l], row[r] = row[r] ^ 1, row[l] ^ 1
			l += 1
			r -= 1

	return image
 '''
