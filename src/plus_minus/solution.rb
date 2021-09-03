def get_signs(number, condition)
    if condition
        return number
    else
        return -number
    end
 end
 
 def solution(absolutes, signs)
     
     answer = 0
     
     for i in 0...absolutes.length
         answer += get_signs(absolutes[i], signs[i])
     end
     
     return answer
 end