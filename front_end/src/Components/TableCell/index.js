import React, {Fragment, useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { SET_EDITING_CELL } from '../../Reducers/Edit'
import {
    getCellId,
    postData,
    processForecastData,
    formatValue
} from '../../Util'
import { SET_ERROR } from '../../Reducers/Error'
import { SET_CELLS } from '../../Reducers/Cells'

const TableCell = ({rowIndex, cellKey, sheetUpdating}) => {
    const dispatch = useDispatch();

    const cells = useSelector(state => state.allCells.cells);
    const cell = useSelector(state => state.allCells.cells[rowIndex][cellKey]);
    const editCellId = useSelector(state => state.edit.cellId);

    const [isUpdating, setIsUpdating] = useState(false)

    const selectedRow = useSelector(state => state.selected.selectedRow);
    const allSelected = useSelector(state => state.selected.all);

    const cellId = getCellId(rowIndex, cellKey)

    let isEditable = true

    // Check for actual
    if (window.actuals.indexOf(cellKey) > -1) {
        isEditable = false
    }

    const getValue = () => {
        if (cell && cell.amount) {
            return (cell.amount / 100).toFixed(2)
        } else {
            return "0.00"
        }
    }

    const [value, setValue] = useState(getValue())

    useEffect(() => {
        if (cell) {
            setValue((cell.amount / 100).toFixed(2))
        }
    }, [cell]);

    const isSelected = () => {
        if (allSelected) {
            return true
        }

        return selectedRow === rowIndex
    }

    const wasEdited = () => {
        if (!isEditable)
            return false

        return cell.amount !== cell.startingAmount
    }

    const getClasses = () => {
        let editable = ''

        if (!isEditable) {
            editable = ' not-editable'
        }

        if (!cell)
            return "govuk-table__cell forecast-month-cell " + (isSelected() ? 'selected' : '') + editable

        let negative = ''

        if (cell.amount < 0) {
            negative = " negative"
        }

        return "govuk-table__cell forecast-month-cell " + (wasEdited() ? 'edited ' : '') + (isSelected() ? 'selected' : '')  + editable + negative
    }

    const setContentState = (value) => {
        var re = /^-?\d*\.?\d{0,12}$/; 
        var isValid = (value.match(re) !== null);

        if (!isValid) {
            return
        }
        setValue(value)
    }


    const updateValue = () => {
        let newAmount = parseInt(value * 100)

        if (cell && newAmount === cell.amount) {
            return
        }

        setIsUpdating(true)

        let payload = new FormData()
        payload.append("natural_account_code", cells[rowIndex]["natural_account_code"].value)
        payload.append("programme_code", cells[rowIndex]["programme"].value)
        payload.append("project_code", cells[rowIndex]["project_code"].value)
        payload.append("analysis1_code", cells[rowIndex]["analysis1_code"].value)
        payload.append("analysis2_code", cells[rowIndex]["analysis2_code"].value)

        payload.append("month", cellKey)
        payload.append("amount", newAmount)

        postData(
            `/forecast/update-forecast/${window.cost_centre}/`,
            payload
        ).then((response) => {
            setIsUpdating(false)
            if (response.status === 200) {
                let rows = processForecastData(response.data)
                  dispatch({
                    type: SET_CELLS,
                    cells: rows
                  })
            } else {
                dispatch(
                    SET_ERROR({
                        errorMessage: response.data.error
                    })
                );
            }
        })
    }

    const handleBlur = (event) => {
        updateValue()
        dispatch(
            SET_EDITING_CELL({
                "cellId": null
            })
        )
    }

    const handleKeyDown = (event) => {
        if (event.key === "Tab") {
            updateValue()
        }
    }

    const handleKeyPress = (event) => {
        if(event.key === 'Enter') {
            updateValue()
            event.preventDefault()
        }
    }

    const getId = () => {
        if (!cell)
            return

        if (isUpdating) {
            return cellId + "_updating"
        }

        return cellId
    }

    const isCellUpdating = () => {
        if (cell && !isEditable)
            return false

        if (isUpdating)
            return true

        if (sheetUpdating && isSelected()) {
            return true
        }

        return false
    }

    return (
        <Fragment>
            <td
                className={getClasses()}
                id={getId()}
                onDoubleClick={ () => {
                    if (isEditable) {
                        dispatch(
                            SET_EDITING_CELL({
                                "cellId": cellId
                            })
                        );
                    }
                }}
            >
                {isCellUpdating() ? (
                    <Fragment>
                        <span className="updating">UPDATING...</span>
                    </Fragment>
                ) : (
                    <Fragment>
                        {editCellId === cellId ? (
                            <input
                                ref={input => input && input.focus() }
                                id={cellId + "_input"}
                                className="cell-input"
                                type="text"
                                value={value}
                                onChange={e => setContentState(e.target.value)}
                                onKeyPress={handleKeyPress}
                                onKeyDown={handleKeyDown}
                                onBlur={handleBlur}
                            />
                        ) : (
                            <Fragment>{formatValue(getValue())}</Fragment>
                        )}
                    </Fragment>
                )}
            </td>
        </Fragment>
    );
}

export default TableCell
