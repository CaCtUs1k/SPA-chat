function insertTag(openTag, closeTag) {
  const textArea = document.querySelector('textarea');
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