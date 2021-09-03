def solution(s)
    
    eng_hash = {
        :zero => '0',
        :one => '1',
        :two => '2',
        :three => '3',
        :four => '4',
        :five => '5',
        :six => '6',
        :seven => '7',
        :eight => '8',
        :nine => '9'
    }
    
    eng_hash.each do |key, value|
        
        s.gsub!(key.to_s, value.to_s)
        
    end
    
    answer = s.to_i
    return answer
end