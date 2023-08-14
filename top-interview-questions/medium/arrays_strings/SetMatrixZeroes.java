import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
 */

class SetMatrixZeroes {
  public static void main(String[] args) {
    var input = new int[][] { { 0, 1, 2, 0 }, { 3, 4, 5, 2 }, { 1, 3, 1, 5 } };
    var expected = new int[][] { { 0, 0, 0, 0 }, { 0, 4, 5, 0 }, { 0, 3, 1, 0 } };

    var instance = new SetMatrixZeroes();

    instance.setZeroes(input);

    System.out.println(Arrays.deepEquals(input, expected));
  }

  public void setZeroes(int[][] matrix) {
    // setZeroesLinearSpace(matrix);
    setZeroesConstantSpace(matrix);
  }

  private void setZeroesConstantSpace(int[][] matrix) {
    // the idea: when we face matrix[i][j] == 0, we set i-th row and j-th col to
    // zeroes

    int col0 = 1;

    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;
          if (j != 0) {
            matrix[0][j] = 0;
          } else {
            col0 = 0;
          }
        }
      }
    }

    for (int i = 1; i < matrix.length; i++) {
      for (int j = 1; j < matrix[0].length; j++) {
        if (matrix[i][0] == 0 || matrix[0][j] == 0) {
          matrix[i][j] = 0;
        }
      }
    }

    if (matrix[0][0] == 0) {
      for (var j = 1; j < matrix[0].length; j++) {
        matrix[0][j] = 0;
      }
    }

    if (col0 == 0) {
      for (var i = 0; i < matrix.length; i++) {
        matrix[i][0] = 0;
      }
    }
  }

  private void setZeroesLinearSpace(int[][] matrix) {
    Set<Integer> rows = new HashSet<>();
    Set<Integer> cols = new HashSet<>();

    for (var i = 0; i < matrix.length; i++) {
      for (var j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] == 0) {
          rows.add(i);
          cols.add(j);
        }
      }
    }

    for (var row : rows) {
      for (var i = 0; i < matrix[row].length; i++) {
        matrix[row][i] = 0;
      }
    }

    for (var col : cols) {
      for (var i = 0; i < matrix.length; i++) {
        matrix[i][col] = 0;
      }
    }
  }
}