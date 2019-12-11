ERROR_MAPPING = {
    11: "Initial variable values should be a list in the following format:\n" +
        "<VARIABLE>=<INT VALUE>\n" +
        "Space after and before the = will lead to the error!\n"
};

EXAMPLES = {
    recursion: {
        code: `program
func pow(a, b) = 
   if b = 0 
     then 1
     else a * pow(a, b - 1)
begin
    C:= pow(A, B)
end`,
        env: `A=2\nB=10`
    },
    while_and_if: {
        code: `program
func mod(a, b) = a - b * (a / b)
begin
    I := 2;
    isPrime := 1;

    while (I * I <= N) and (isPrime = 1) do
    begin
        if mod(N, I) = 0 then
        begin
            isPrime := 0 
        end;
        I := I + 1 
    end
end`,
        env: `N=17`,
    }
};


function getErrorText(data){
    let code = data['error_code'];
    return  message = ERROR_MAPPING[code] || data['stderr'];
}

function setProgramExample(example_id){
    $('#program').val(EXAMPLES[example_id].code);
    $('#env').val(EXAMPLES[example_id].env);
    $('#result').val('');
}

$(
function () {
    $('#run').click(() => {
        $('#run')
            .removeClass('btn-primary')
            .addClass('btn-info')
            .attr('value', 'Loading...');

        let program_text = $('#program').val();
        let evn_data = $('#env').val();
        $.ajax({
            type: 'POST',
            url: '/run',
            dataType: 'json',
            data: JSON.stringify({
                program: program_text,
                env: evn_data,
            }),
            success: (data, status, jqXHR) => {
                let ok = data['ok'];
                let button = $('#run');
                let result = $('#result');
                if(!ok){
                    button
                        .removeClass('btn-info')
                        .addClass('btn-danger')
                        .attr('value', 'Something went wrong');
                    let errorText = getErrorText(data);
                    result.val(errorText);
                    return;
                }
                button
                    .removeClass('btn-info')
                    .addClass('btn-primary')
                    .attr('value', 'RUN!');
                result.val(data['stdout']);
            },
            error: (data, status, jqXHR) => {
                $('#run')
                    .removeClass('btn-info')
                    .addClass('btn-danger')
                    .attr('value', 'Something went wrong');
                $('#resu')
            }
        })
    });
}
);