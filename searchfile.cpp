#include <iostream>
#include <string>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
using namespace std;
void searchFile(const string& dirPath, const string& targetFile) {
DIR* dir = opendir(dirPath.c_str());
if (!dir) {
perror(("Cannot open directory: " + dirPath).c_str());
return;
}
struct dirent* entry;
while ((entry = readdir(dir)) != nullptr) {
string name = entry->d_name;
// Skip "." and ".."
if (name == "." || name == "..")
continue;
string fullPath = dirPath + "/" + name;
struct stat fileStat;
if (stat(fullPath.c_str(), &fileStat) == -1) {
perror(("Stat failed for: " + fullPath).c_str());
continue;
}
if (S_ISDIR(fileStat.st_mode)) {
// Recurse into subdirectory
searchFile(fullPath, targetFile);
} else if (name == targetFile) {
cout << "Found: " << fullPath << endl;
}
}
closedir(dir);
}
int main(int argc, char* argv[]) {
if (argc != 3) {
cout << "Usage: " << argv[0] << " <start_directory> <file_name>" <<
endl;
return 1;
}
string startDir = argv[1];
string targetFile = argv[2];
searchFile(startDir, targetFile);
return 0;
}