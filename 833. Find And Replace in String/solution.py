class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        sorted_tokens = sorted(
            zip(indices, sources, targets),
            key=lambda t: t[0])
        indices, sources, targets = list(zip(*sorted_tokens))

        res = s
        total_diff = 0
        for (i, idx) in enumerate(indices):
            idx = indices[i]
            src = sources[i]
            src_len = len(src)
            tgt = targets[i]
            if s[idx:idx+src_len] == src:
                offset = idx + total_diff
                res = res[:offset] + tgt + res[offset+src_len:]
                total_diff += len(tgt) - src_len

        return res
