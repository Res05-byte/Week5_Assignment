int dot(int* a, int* b, int n)
{
    int i;
    int total = 0;

    for(i = 0; i < n; i++)
    {
        total += a[i] * b[i];
    }

    return total;
}