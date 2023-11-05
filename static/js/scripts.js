const decimalValueInput = document.querySelector('input[name="decimal_value"]');
const integerValueInput = document.querySelector('input[name="integer_value"]');
const ratioInput = document.querySelector('input[name="ratio');

const decimalValueOutput = document.querySelector('output[for="decimal_value"]');
const ratioOutput = document.querySelector('output[for="ratio"]');

decimalValueInput.addEventListener('input', function () {
    decimalValueOutput.textContent = this.value;
});

ratioInput.addEventListener('input', function () {
    ratioOutput.textContent = this.value;
});