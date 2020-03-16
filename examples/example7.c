int main() {
    int exitstatus = -1;
    int x = 1;
    int y = 99;

    if (x <= y) {
        exitstatus = 0;
    } else {
        exitstatus = 9999;
    }

    return exitstatus;
}
