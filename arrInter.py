class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        intersection = []
        len1 = len(nums1)
        len2 = len(nums2)
        a,b = 0, 0
        # print(n1, "with length", len(nums1))
        # print(n2, "with length", len(nums2))
        while a < len1 and b < len2:
            if n1[a] < n2[b]:
                # print("increasing a")
                a +=1
            elif n2[b] < n1[a]:
                # print("increasing b")
                b +=1
            else:
                # print("adding value %s to intersecrtion array"%(n1[a]))
                intersection.append(n1[a])
                a +=1
                b +=1
            # print(intersection)
        return intersection
                
        