class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        for f in sorted(folder):
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        seen, res = [], []
        for path in folder:
            if not path or path == '/':
                continue
            for pre_path in seen:
                if path.startswith(pre_path + '/'):
                    break
            else:
                seen.append(path)
                res.append(path)
        return res
'''
nlog because of sort
'''