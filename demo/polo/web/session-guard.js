// A reply belongs to an exact tab session, person, design and generation.
export function acceptsTryOn(captured, current, returnedRevision) {
  return captured.session === current.session &&
    captured.person === current.person &&
    captured.revision === current.revision &&
    captured.job === current.job &&
    returnedRevision === captured.revision;
}
