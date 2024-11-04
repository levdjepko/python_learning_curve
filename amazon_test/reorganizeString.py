class Solution:
    def reorganizeString(self, s: str) -> str:
        # we have a frequency of each character in original string
        char_freq = {}
        for char in s:
            if char in char_freq:
                frequency = char_freq[char]
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        print(str(char_freq))            
        
        # append the tuples with -freq for each char into the heap
        max_heap = [(-frequency, char) for char, frequency in char_freq.items()]
        heapq.heapify(max_heap)

        res = []
        prev_freq = 0
        prev_char = ""

        while max_heap:
            frequency, char = heapq.heappop(max_heap)
            res.append(char)
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            frequency += 1
            prev_freq, prev_char = frequency, char
        if len(res) != len(s):
            return ""
        else:
            return "".join(res)          
