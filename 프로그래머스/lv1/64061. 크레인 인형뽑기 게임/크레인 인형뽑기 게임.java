class Solution {
    public int solution(int[][] board, int[] moves) {
        int[] temp = new int[moves.length];
        int t = 0;
        int answer = 0;
        
        for(int i = 0; i < moves.length; i++) {
            for(int j = 0; j < board.length; j++) {
                if(board[j][moves[i] - 1] != 0) {
                    temp[t] = board[j][moves[i] - 1];
                    board[j][moves[i] - 1] = 0;
                    if(t > 0 && (temp[t] == temp[t - 1])) {
                        temp[t] = 0;
                        temp[t - 1] = 0;
                        if(t >= 2) t -= 2;
                        else t -= 1;
                        answer += 2;
                    }
                    break;
                }

            }
            if(temp[t] != 0) t++;
        }
        return answer;
    }
}