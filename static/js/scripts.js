function insertTag(openTag, closeTag, button) {
  const form = button.closest('form');
  const textArea = form.querySelector('textarea');
  const startPos = textArea.selectionStart;
  const endPos = textArea.selectionEnd;

  const selectedText = textArea.value.substring(startPos, endPos);
  const replacement = `${openTag}${selectedText}${closeTag}`;

  textArea.value =
    textArea.value.substring(0, startPos) +
    replacement +
    textArea.value.substring(endPos, textArea.value.length);

  textArea.focus();
  textArea.setSelectionRange(startPos + openTag.length, startPos + openTag.length + selectedText.length);
}

function validateForm(form) {
  const textArea = form.querySelector('textarea');
  const commentText = textArea.value;

  const openTagCount = (commentText.match(/<[^/]/g) || []).length;
  const closeTagCount = (commentText.match(/<\/[^/]/g) || []).length;

  if (openTagCount === closeTagCount) {
    return true;
  } else {
    alert('Please make sure all tags are closed correctly.');
    return false;
  }
}

function SwitchReply(parent_id) {
    const switch_form_visibility = document.querySelector(`.switch-form-visibility-${parent_id}`)
    const show_form_button = document.querySelector(`#show-form-button-${parent_id}`)

    if (switch_form_visibility) {
        if (switch_form_visibility.style.display === 'block') {
            switch_form_visibility.style.display = 'none';
            show_form_button.innerText = "Reply"
        }
        else {
            switch_form_visibility.style.display = 'block';
            show_form_button.innerText = "Discard"
        }
    }
}

function SwitchNewThread() {
    const switch_form_visibility = document.querySelector(`.switch-form-visibility`)
    const show_form_button = document.querySelector(`#show-form-button`)

    if (switch_form_visibility) {
        if (switch_form_visibility.style.display === 'block') {
            switch_form_visibility.style.display = 'none';
            show_form_button.innerText = "Reply"
        }
        else {
            switch_form_visibility.style.display = 'block';
            show_form_button.innerText = "Discard"
        }
    }
}