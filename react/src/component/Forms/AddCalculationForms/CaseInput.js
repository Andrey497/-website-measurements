import InputNumber from "./Inputs/InputNumber";
import InputNumrange from "./Inputs/InputNumrange";
import InputString from "./Inputs/InputString";
import InputFunction from "./Inputs/InputFunction";

const CaseInput = (props) => {
    let inputCase = null;
    switch (props.id_data) {
        case 1:
            console.log('caseInput');
           inputCase= <InputNumber value={props.value} id_value = {props.id_value}/>
            break;
        case 2:
            inputCase=  <InputNumrange/>
            break;
        case 3:
            inputCase= <InputString />
            break;
        case 4:
            inputCase= <InputFunction/>
            break;
    }
    return (

        <div>
            {inputCase}
        </div>
    )
}
export  default CaseInput

