// AoC2022 - day 4
//
// ZX Spectrum version
//
// compile with z88dk, e.g.:
// zcc +zx -lndos -create-app day4.c
//
// load the resulting a.tap into your favourite speccy emulator (Fuse?) (or create a WAV and use the Real Thing)
//
// POKE 32767,n (n=0 for puzzle 1, n!=0 for puzzle 2)
// PRINT USR 32768 (to get result)
//
// by default the program is loaded very high in memory, leaving a little under 16k for program and data
// real test data is 1000 lines, which just fits. :-)

const char *test[] = {
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
    0};

#define NUM_INTS 4
#define PUZZLE_LOCATION (32767) // POKE a 0 here for puzzle 1, or non-zero for puzzle 2

int main()
{
       int n = 0;                              // line counter
       int count = 0;                          // result counter
       const char *s;                          // character pointer
       while ((s = test[n++]))
       {
              unsigned int r[NUM_INTS] = {0, 0, 0, 0};
              unsigned char r_n = 0; // value counter

              char c;
              while ((c = *s++))
              {
                     if ((c >= '0') && (c <= '9'))
                            r[r_n] = (r[r_n] * 10) + (c - '0');
                     else
                     {
                            r_n++;
                            if (r_n == NUM_INTS) // just wrap if there appear to be too many numbers on a line
                                   r_n = 0;
                     }
              }

              if (r_n == NUM_INTS - 1) // only do this bit if we have four numbers: (left_min,left_max)=(r[0],r[1]); (right_min,right_max)=(r[2],r[3])
              {
                     if (*(char *)PUZZLE_LOCATION == 0)
                     {
                            if (r[1] >= r[2] && r[0] <= r[3]) // test overlap
                                   count++;
                     }
                     else
                     {
                            if ((((r[2] >= r[0]) && (r[2] <= r[1])) && ((r[3] >= r[0]) && (r[3] <= r[1]))) || (((r[0] >= r[2]) && (r[0] <= r[3])) && ((r[1] >= r[2]) && (r[1] <= r[3])))) // test one range contains the other
                                   count++;
                     }
              }
       }
       return count; // becomes the retval of the USR function
}
